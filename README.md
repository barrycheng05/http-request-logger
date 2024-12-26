# HTTP Request Logger

A lightweight HTTP request logging server built with Flask that captures and logs detailed information about incoming HTTP requests, including method, URL, headers, and body content. Containerized with Docker and deployable to Kubernetes, making it ideal for debugging, testing, and monitoring HTTP traffic in development and staging environments.

## Features

- Logs all incoming HTTP requests (GET, POST, PUT, DELETE, PATCH)
- Captures request details including:
  - HTTP method
  - URL
  - Headers
  - Request body
- Runs in a Docker container
- Includes Kubernetes deployment configuration
- Responds to all paths (`/*`)
- Returns 200 OK for all requests

## Prerequisites

- Python 3.9+
- Docker
- Kubernetes cluster (optional)

## Quick Start

### Running Locally

1. Clone the repository:
```bash
git clone https://github.com/yourusername/http-request-logger.git
cd http-request-logger
```

2. Run with Python:
```bash
python request_logger.py
```

The server will start on `http://localhost:8080`

### Running with Docker

1. Build the Docker image:
```bash
docker build -t http-request-logger .
```

2. Run the container:
```bash
docker run -p 8080:8080 http-request-logger
```

### Deploying to Kubernetes

1. Apply the Kubernetes configuration:
```bash
kubectl apply -f k8s.yaml
```

2. Verify the deployment:
```bash
kubectl get pods
kubectl get services
```

## Usage

Send any HTTP request to the server, and it will log the details:

```bash
# Example using curl
curl -X POST http://localhost:8080/test -H "Content-Type: application/json" -d '{"test": "data"}'
```

Example log output:
```
2024-12-26 10:00:00,000 - INFO - === New Request ===
2024-12-26 10:00:00,000 - INFO - Method: POST
2024-12-26 10:00:00,000 - INFO - URL: http://localhost:8080/test
2024-12-26 10:00:00,000 - INFO - Headers: {'Content-Type': 'application/json', ...}
2024-12-26 10:00:00,000 - INFO - Body: {"test": "data"}
```

## Project Structure

```
.
├── Dockerfile           # Docker configuration file
├── dump_server.py      # Main Flask application
├── k8s.yaml            # Kubernetes deployment configuration
└── README.md           # This file
```

## License

This project is licensed under the MIT License - see the LICENSE file for details.
