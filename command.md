pip freeze >> requirements.txt
chmod +x ./entrypoint.sh
docker-compose up --build
docker exec -it django /bin/sh 
#django refers to container_name