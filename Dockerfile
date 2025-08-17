FROM python:3.12-slim

WORKDIR /app


# Instalar dependencias del sistema necesarias para mysqlclient
RUN apt-get update \
	&& apt-get install -y --no-install-recommends gcc default-libmysqlclient-dev pkg-config \
	&& rm -rf /var/lib/apt/lists/*

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["uvicorn", "api.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
