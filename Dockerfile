# FROM python:3.11.4-alpine

# # prevent Python from writing •pyc files
# ENV PYTHONDONTWRITEBYTECODE 1
# # ensure Python output is sent directly to the terminal with
# ENV PYTHONUNBUFFERED 1
# RUN pip install --upgrade pip
# COPY requirements.txt /usr/src/app/requirements.txt
# RUN pip install -r requirements.txt

# COPY entrypoint.sh /usr/src/app/entrypoint.sh


# COPY . /usr/src/app/

# ENTRYPOINT [ "/usr/src/app/entrypoint.sh" ]

# Use the official Python image from the Docker Hub
FROM python:3.11.4-alpine

# Set the working directory
WORKDIR /usr/src/app

# Copy the requirements file into the container
COPY requirements.txt /usr/src/app/

# Install dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copy the rest of the application code into the container
COPY . /usr/src/app/

# Specify the command to run on container start
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
