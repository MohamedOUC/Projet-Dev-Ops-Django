
# Utiliser une image python comme base
FROM python:3.10

# Définir le répertoire de travail
WORKDIR /app

# Copier et installer les dépendances
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copier l'application Django
COPY . /app

# Exposer le port Django
EXPOSE 8000

# Lancer Gunicorn pour exécuter Django
CMD ["gunicorn", "--chdir", "/app", "django_project.wsgi:application", "--bind", "0.0.0.0:8000"]

