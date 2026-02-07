.PHONY: install install-dev lint test run docker-build docker-run

install:
	pip install -r requirements.txt

install-dev:
	pip install -r requirements-dev.txt

lint:
	ruff check .

test:
	pytest

run:
	gunicorn --bind 0.0.0.0:8000 --workers 2 wsgi:app

docker-build:
	docker build -t flask-devops-showcase:latest .

docker-run:
	docker run --rm -p 8000:8000 flask-devops-showcase:latest
