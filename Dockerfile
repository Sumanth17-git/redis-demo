# Use Python as the base image
FROM python:3.9

# Set working directory inside the container
WORKDIR /app

# Copy the ingestion script
COPY ingest_redis.py .

# Install Redis client library
RUN pip install redis

# Run the script when the container starts
CMD ["python", "ingest_redis.py"]
