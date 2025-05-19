# Use Python base image
FROM python:3.10-slim

# Set working directory inside container
WORKDIR /app

# Copy all project files
COPY . /app

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose port Flask runs on
EXPOSE 5000

# Run the app
CMD ["python", "app.py"]
