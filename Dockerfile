# Lightweight Python image
FROM python:3.12-slim

# Environment settings
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Working directory
WORKDIR /app

# Copy dependency file first (better layer caching)
COPY requirements.txt .

# Install dependencies
RUN pip install --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY calculator.py .

# Run application
CMD ["python", "calculator.py"]

# Purpose of requirements.txt putting before pip install and calculator.py: To utilize Docker layer caching. 
# Dependencies are installed only when requirements.txt changes, 
# improving build performance in CI/CD pipelines.