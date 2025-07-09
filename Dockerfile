# Usa una imagen base de Python
FROM python:3.11-slim

# Instala las dependencias del sistema necesarias incluyendo Node.js
RUN apt-get update && apt-get install -y \
    unzip \
    curl \
    git \
    nodejs \
    npm \
    && rm -rf /var/lib/apt/lists/*

# Establece el directorio de trabajo
WORKDIR /app

# Copia los archivos de requirements
COPY requirements.txt .

# Instala las dependencias de Python
RUN pip install --no-cache-dir -r requirements.txt

# Copia el resto del código
COPY . .

# Inicializa el proyecto Reflex
RUN reflex init

# Expone el puerto 3000 (que es el que Railway tiene configurado)
EXPOSE 3000

# Comando para ejecutar la aplicación completa en modo producción
# Frontend y backend en el mismo puerto que Railway espera
CMD ["reflex", "run", "--env", "prod", "--frontend-port", "3000", "--backend-port", "3000", "--backend-host", "0.0.0.0"]