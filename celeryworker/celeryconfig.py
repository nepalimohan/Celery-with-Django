# import os

# CELERY_BROKER_URL = os.environ.get("CELERY_BROKER", "redis://redis:6379/0") #0 refers to default db
# CELERY_RESULT_BACKEND = os.environ.get("CELERY_BACKEND", "redis://redis:6379/0") #0 refers to default db

# celeryworker/celeryconfig.py
# celeryworker2/celeryconfig.py

from celery import Celery

# Define the Celery application instance
app = Celery('celeryworker')

# Load configuration from Django settings
app.config_from_object('settings', namespace='CELERY')

# Automatically discover tasks in all Django apps
app.autodiscover_tasks()
