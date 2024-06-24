pip freeze >> requirements.txt
chmod +x ./entrypoint.sh
docker-compose up -d --build

python manage.py shell

docker exec -it django /bin/sh 
#django refers to container_name



in celery worker, instead of replicating the celeray_app func
we just create a file system identical in celeryworker


if you look at celery.py, the tasks are queued and the queue tasks are segregated to celery in django and celeryworker


tp1. delay ( )
from
celery import group
from newapp. tasks import tpl, tp2, tp3, tp4, tps, taskl
task_group = group(tpl.s(), tp2.s(), tp3.s(), tp4.s())
task_group-apply_async()