# Use an official Python runtime as a parent image
FROM python:3.11.4-alpine

# Set the working directory
WORKDIR /usr/src/app

# Copy the requirements file into the container
COPY requirements.txt .

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container
COPY . .

# Specify the command to run Celery worker
# CMD ["celery", "-A", "celeryconfig", "worker", "-l", "INFO", "-Q", "queue2"]


#celeryconfig is the filename inside celeryworker