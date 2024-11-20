# Utilisez l'image de base Python
FROM python:3

# Définir le répertoire de travail dans le conteneur
WORKDIR /usr/src/app

# Copier les fichiers du projet dans le conteneur
COPY app.py requirements.txt ./

# Installer les dépendances
RUN pip install --no-cache-dir -r requirements.txt

# Exécuter l'application
CMD ["python", "app.py"]
