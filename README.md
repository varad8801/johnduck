# Flask DevOps Showcase

A production-oriented Flask service scaffold designed to demonstrate practical DevOps capabilities.

## Features

- Flask app factory with environment-based configuration.
- Operational endpoints:
  - `GET /healthz` for liveness.
  - `GET /readyz` for readiness.
  - `GET /metrics` for Prometheus scraping.
- Unit tests with `pytest`.
- Linting with `ruff`.
- Containerized runtime with `Dockerfile` and `docker-compose`.
- CI pipeline via GitHub Actions.
- Kubernetes manifests (`Deployment`, `Service`, `HPA`).

## Local setup

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements-dev.txt
```

## Run locally

```bash
make run
```

App URL: `http://localhost:8000`

## Validate quality

```bash
make lint
make test
```

## Run with Docker

```bash
docker compose up --build
```

## Kubernetes

```bash
kubectl apply -f k8s/
```

> Update the image name/tag in `k8s/deployment.yaml` to match your container registry.
