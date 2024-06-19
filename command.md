pip freeze >> requirements.txt
chmod +x ./entrypoint.sh
docker-compose up -d --build

python manage.py shell

docker exec -it django /bin/sh 
#django refers to container_name