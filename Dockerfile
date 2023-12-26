# Use an official Python runtime as a base image
ARG BASE_IMAGE=python:3.9-slim
FROM ${BASE_IMAGE}

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Make port 8000 available to the world outside this container
EXPOSE 8000

# Define environment variable
ENV APP_NAME python-api-starter-kit

# Run app.py when the container launches
CMD ["python", "main.py"]