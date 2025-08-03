import pika
import json
import uuid
from datetime import datetime
import logging


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)



def send_download_task(file_id):
    try:
        # Enriquecer el mensaje
        enriched = {
            "id": str(uuid.uuid4()),
            "timestamp": datetime.utcnow().isoformat(),
            "file_id": file_id
        }

        logger.info(f"Intentando enviar tarea para file_id: {file_id}")

        connection = pika.BlockingConnection(pika.ConnectionParameters("localhost"))
        channel = connection.channel()
        
        # Declarar la cola
        queue_result = channel.queue_declare(queue='download_queue', durable=True)
        logger.info(f"Cola declarada: {queue_result.method.queue}")

        # Publicar mensaje
        channel.basic_publish(
            exchange='',
            routing_key='download_queue',
            body=json.dumps(enriched),
            properties=pika.BasicProperties(
                delivery_mode=2,  # make message persistent
            )
        )
        
        logger.info(f"Mensaje enviado exitosamente: {json.dumps(enriched)}")
        connection.close()
        
    except Exception as e:
        logger.error(f"Error enviando mensaje a RabbitMQ: {str(e)}")
        raise

