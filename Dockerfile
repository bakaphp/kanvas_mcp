# Use an official Python runtime as a base image
FROM python:3.12-slim
# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set work directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Install pipenv or use requirements.txt (adjust as needed)
COPY requirements.txt /app/requirements.txt 
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy the project files into the container
COPY . /app

ENV PYTHONPATH=/app
# Expose the port your app will run on (adjust if different)
EXPOSE 8080

# Run the server (you can customize this)
CMD ["python", "mcp_server.py"]