from celery import Celery


app = Celery('celeryworker')
# app.config_from_object('celeryconfig')
app.config_from_object('django_celery.settings', namespace='CELERY')

@app.task
def add_numbers():
    return

app.autodiscover_tasks()