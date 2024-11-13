# Use the official Python 3.12.6 slim image based on Debian Bullseye
FROM python:3.12.6-slim-bullseye

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Create a directory for uploads and set permissions
RUN mkdir -p /app/static/uploads && chmod 777 /app/static/uploads

# Make port 8080 available to the world outside this container
EXPOSE 8080

# Define environment variable
ENV FLASK_APP=app.py

# Run app.py when the container launches
CMD ["python", "app.py"]