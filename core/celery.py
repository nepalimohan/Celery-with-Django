import os
from celery import Celery


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
app = Celery("core") #project folder name
app.config_from_object("django.conf:settings", namespace="CELERY")


@app.task
def add_numbers():
    return f"Add Numbers {6}"

app.autodiscover_tasks() #specifying celery to look for all the tasks