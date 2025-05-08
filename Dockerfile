# Use the official Python image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container
COPY . /app

# Command to run your Python script
CMD ["python", "Wumpus.py"]