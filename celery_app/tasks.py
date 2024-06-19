from celery import shared_task

@shared_task #@app.task will also work but you will have to import it
def shared_task():
    return