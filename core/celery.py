from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from celery.schedules import crontab


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
app = Celery("core") #project folder name
app.config_from_object("django.conf:settings", namespace="CELERY")
# app.conf.task_routes = {'celery_app.tasks.task1': {'queue':'queue1'}, 'celery_app.tasks.task2':{'queue':'queue2'}}
app.autodiscover_tasks() #specifying celery to look for all the tasks


app.conf.broker_transport_options = {
    'priority_steps': list(range(10)),
    'sep': ':',
    'queue_order_strategy': 'priority',
}


# app.conf.beat_schedule = {
#     'send-scheduled-email-every-minute': {
#         'task': 'celery_app.tasks.send_email_task',  # Replace with correct path to your task
#         'schedule': crontab(minute='*/1'),  # Schedule the task to run every minute
#         'args': ('Scheduled Email', 'This is a scheduled email.', 'nepali.mohan11@gmail.com', ['nepalimohan.spices@gmail.com']),
#     },
# }


