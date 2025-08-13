# Base image with Python
FROM python:3.9-slim

# Set working directory inside container
WORKDIR /app

# Copy all project files into container
COPY . /app

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose Airflow webserver port
EXPOSE 8080

# Default command (can be changed when running)
CMD ["airflow", "webserver"]
