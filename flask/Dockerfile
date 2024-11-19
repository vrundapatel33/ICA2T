
## Use python:3.9-slim as base image
FROM python:3.9-slim

# Set the working directory inside the container to /flask
WORKDIR /flask

# Copy the requirements file into the container and install dependencies
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the Flask application code (app.py) into the container at /flask
COPY app.py /flask/app.py

# Expose the port that Flask will run on
EXPOSE 5000

# Define the command to run the Flask application
CMD ["python", "app.py"]
