# Basis-Image
FROM python:3.11-slim

# Arbeitsverzeichnis im Container
WORKDIR /app

# Kopiere alle Dateien ins Image
COPY . .

# Installiere Python-Abhängigkeiten
RUN pip install --no-cache-dir -r requirements.txt

# Freigegebener Port
EXPOSE 5000

# Startbefehl
CMD ["python", "main.py"]
LABEL org.opencontainers.image.source https://github.com/1levin7/zu-bbbearbeiten-stateless

