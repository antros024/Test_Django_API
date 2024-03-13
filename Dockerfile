# Use an official Python runtime as a parent image
FROM python:3.11

# Set environment variables
ENV PYTHONUNBUFFERED=1

# Set the working directory in the container
WORKDIR /Test_Django_API

COPY requirements.txt .

# Install any dependencies specified in requirements.txt
RUN pip install -r requirements.txt

COPY . .

# Expose port 8000 to allow external access
EXPOSE 8000

# Command to run the Django development server
CMD ["python", "manage.py", "runserver"]
