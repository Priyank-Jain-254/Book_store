# Use official Python 3.11 slim image
FROM python:3.11.8-slim

# Prevent Python from writing .pyc files
ENV PYTHONDONTWRITEBYTECODE 1

# Prevent Python from buffering stdout/stderr
ENV PYTHONUNBUFFERED 1

# Set working directory in the container
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the project files into the container
COPY . .

# Expose port for Django
EXPOSE 8000

# Command to run the app
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
