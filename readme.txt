python manage.py commands will not work here as settings is 
using secret key and other info from environment variables


When working with celery, do not forget to specify/initialize initialize
it in __init__.py file, else it will give you connection error

https://www.youtube.com/watch?v=xTGbfrdiv4U&list=PLOLrQ9Pn6cayGytG1fgUPEsUp3Onol8V7&index=8