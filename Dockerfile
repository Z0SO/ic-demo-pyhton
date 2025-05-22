# Imagen base de Python
FROM python:3.11-slim

# EL workdir es el directorio de trabajo dentro del contenedor
WORKDIR /app
COPY app.py .
COPY requirements.txt .
COPY test_app.py .

# --no-cache-dir evita que pip almacene en caché los paquetes descargados
RUN pip install --no-cache-dir -r requirements.txt

# CMD es el comando que se ejecuta al iniciar el contenedor
CMD ["python", "app.py"]
