from flask import Flask, jsonify
from prometheus_flask_exporter import PrometheusMetrics
import random

app = Flask(__name__)
metrics = PrometheusMetrics(app)

@app.route("/health")
def health():
    if random.random() < 0.1:
        return jsonify(status="unhealthy"), 500
    return jsonify(status="healthy"), 200

@app.route("/")
def home():
    return "Hello, SRE World!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
