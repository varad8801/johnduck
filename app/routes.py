import os
import time

from flask import Flask, jsonify
from prometheus_client import CONTENT_TYPE_LATEST, Counter, generate_latest

START_TIME = time.time()
REQUEST_COUNTER = Counter("http_requests_total", "Total HTTP requests", ["endpoint"])


def register_routes(app: Flask) -> None:
    @app.get("/")
    def index():
        REQUEST_COUNTER.labels(endpoint="/").inc()
        return jsonify(
            {
                "service": app.config.get("SERVICE_NAME", "flask-devops-showcase"),
                "environment": app.config.get("ENVIRONMENT", "dev"),
                "message": "Flask DevOps showcase is running",
            }
        )

    @app.get("/healthz")
    def healthz():
        REQUEST_COUNTER.labels(endpoint="/healthz").inc()
        return jsonify({"status": "ok"})

    @app.get("/readyz")
    def readyz():
        REQUEST_COUNTER.labels(endpoint="/readyz").inc()
        dependencies = {
            "required_env": bool(os.getenv("APP_ENVIRONMENT", "dev")),
        }
        ready = all(dependencies.values())
        return jsonify({"ready": ready, "checks": dependencies}), (200 if ready else 503)

    @app.get("/metrics")
    def metrics():
        REQUEST_COUNTER.labels(endpoint="/metrics").inc()
        uptime_seconds = time.time() - START_TIME
        payload = generate_latest() + f"app_uptime_seconds {uptime_seconds}\n".encode()
        return payload, 200, {"Content-Type": CONTENT_TYPE_LATEST}
