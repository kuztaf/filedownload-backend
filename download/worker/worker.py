import pika
import json
import time
from pathlib import Path
import sys
import logging

# Configurar logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Permite importar desde app/report_store.py
sys.path.append(str(Path(__file__).resolve().parents[1]))

from api.models.document import Document
from api.db.database import SessionLocal

def process_report(file_id: str):
    logger.info(f"📌 Procesando documento {file_id}")
    session = SessionLocal()
    try:
        document = session.query(Document).filter(Document.id == int(file_id)).first()
        if not document:
            logger.error(f"❌ Documento con ID {file_id} no encontrado en la base de datos.")
            return
        if not document.content:
            logger.error(f"❌ El documento {file_id} no tiene archivo guardado en el campo 'content'.")
            return
        logger.info(f"✅ Documento encontrado. Tamaño del archivo: {len(document.content)} bytes")
        # Aquí puedes procesar el archivo, por ejemplo guardarlo en disco:
        output_path = f"/tmp/document_{file_id}.bin"
        with open(output_path, 'wb') as f:
            f.write(document.content)
        logger.info(f"📄 Archivo guardado en: {output_path}")
    except Exception as e:
        logger.error(f"❌ Error accediendo a la base de datos o procesando el archivo: {str(e)}")
    finally:
        session.close()

def callback(ch, method, properties, body):
    try:
        message = body.decode()
        logger.info(f"📨 Mensaje recibido: {message}")
        # Intentar parsear como JSON
        try:
            data = json.loads(message)
            if isinstance(data, dict) and "file_id" in data:
                file_id = data["file_id"]
                logger.info(f"🔍 Procesando file_id desde JSON: {file_id}")
                process_report(file_id)
            else:
                logger.warning(f"⚠️ Mensaje JSON no contiene 'file_id': {data}")
        except json.JSONDecodeError:
            # Fallback al formato anterior
            if message.startswith("generate_report:"):
                file_id = message.split(":")[1]
                logger.info(f"🔍 Procesando file_id desde formato legacy: {file_id}")
                process_report(file_id)
            else:
                logger.warning(f"⚠️ Formato de mensaje desconocido: {message}")
        ch.basic_ack(delivery_tag=method.delivery_tag)
    except Exception as e:
        logger.error(f"❌ Error procesando mensaje: {str(e)}")
        ch.basic_nack(delivery_tag=method.delivery_tag, requeue=False)

def main():
    connection = pika.BlockingConnection(pika.ConnectionParameters("localhost"))
    channel = connection.channel()

    # channel.queue_declare(queue='report_queue', durable=True)
    channel.queue_declare(queue='report_queue', durable=True, exclusive=False, auto_delete=False)
    channel.basic_qos(prefetch_count=1)
    channel.basic_consume(queue='report_queue', on_message_callback=callback)

    print("👷 Worker escuchando tareas...")
    channel.start_consuming()

if __name__ == "__main__":
    main()