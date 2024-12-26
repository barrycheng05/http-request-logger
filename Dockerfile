FROM python:3.9-slim

# Install Flask
RUN pip install flask

# Copy the Flask application to the container
WORKDIR /app
COPY request_logger.py .

# Expose the default Flask port 8080
EXPOSE 8080

# Start the Flask application
CMD ["python", "request_logger.py"]