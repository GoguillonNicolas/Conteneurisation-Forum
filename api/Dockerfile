FROM python:3.11-slim

WORKDIR /app

# Installation des dependances
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copie du code source
COPY . .

# Port expose
EXPOSE 5000

# Commande par defaut pour lancer le serveur Flask
CMD ["python", "app.py"]
