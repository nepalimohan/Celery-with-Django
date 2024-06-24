python manage.py commands will not work here as settings is 
using secret key and other info from environment variables

Using Redis as a message broker does not support task prioritization.



When working with celery, do not forget to specify/initialize initialize
it in __init__.py file, else it will give you connection error


in celery worker, instead of replicating the celeray_app func
we just create a file system identical in celeryworker


if you look at celery.py, the tasks are queued and the queue tasks are segregated to celery in django and celeryworker


https://www.youtube.com/watch?v=nY3SwOm7Ino&list=PLOLrQ9Pn6cayGytG1fgUPEsUp3Onol8V7&index=19




16th celery vdo