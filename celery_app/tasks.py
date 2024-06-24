from celery import shared_task
from django.core.mail import send_mail
from core import settings
import logging
import time

@shared_task #@app.task will also work but you will have to import it
def task1():
    return "task 1"


@shared_task #@app.task will also work but you will have to import it
def task2():
    return "task 2 "


# your_app/tasks.py
logger = logging.getLogger(__name__)

@shared_task
def send_email_task(subject, message, from_email, recipient_list):
    try:
        send_mail(subject, message, from_email, recipient_list)
        logger.info(f"Email sent to {recipient_list}")
    except Exception as e:
        logger.error(f"Failed to send email: {e}")


@shared_task
def tp1(queue='celery'):
    time.sleep(3)
    return "k tha"

@shared_task
def tp2(queue='celery:1'):
    time.sleep(3)
    return "k tha"


@shared_task
def tp3(queue='celery:2'):
    time.sleep(3)
    return "k tha"


@shared_task
def tp4(queue='celery:3'):
    time.sleep(3)
    return "k tha"

# tp1.delay()
# tp1.delay()
# tp2.delay()
# tp2.delay()
# tp2.delay()
# tp2.delay()
# tp2.delay()
# tp2.delay()
# tp2.delay()
# tp2.delay()
# tp2.delay()
# tp3.delay()
# tp3.delay()
# tp3.delay()
# tp3.delay()
# tp4.delay()
# tp4.delay()
# tp4.delay()
# tp4.delay()
# tp4.delay()