import logging
from flask import Flask, request

# Set logging format
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

app = Flask(__name__)

@app.route('/', defaults={'path': ''}, methods=['GET', 'POST', 'PUT', 'DELETE', 'PATCH'])
@app.route('/<path:path>', methods=['GET', 'POST', 'PUT', 'DELETE', 'PATCH'])
def catch_all(path):
    logging.info("=== New Request ===")
    logging.info(f"Method: {request.method}")
    logging.info(f"URL: {request.url}")
    logging.info(f"Headers: {dict(request.headers)}")
    if request.data:
        logging.info(f"Body: {request.data.decode('utf-8')}")
    else:
        logging.info("Body: <empty>")
    return "Request captured!\n", 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)