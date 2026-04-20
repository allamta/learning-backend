# Learning Backend

Minimal FastAPI backend used to practice Docker and Kubernetes deployment basics.

## What This Project Does

This service exposes:

- `GET /health` for a simple health check
- `POST /api/analyze` for mocked ingredient analysis

The analysis endpoint does basic keyword matching against the submitted text:

- `sugar` -> `unhealthy`
- `oats` -> `healthy`
- `salt` -> `neutral`
- no match -> `Unknown`

This is intentionally simple. The goal of the project is learning containerization and Kubernetes concepts, not building a real nutrition analysis engine.

## Project Structure

```text
.
|-- main.py
|-- tests/
|   `-- test_main.py
|-- Dockerfile
|-- requirements.txt
|-- requirements-dev.txt
`-- README.md
```

## Requirements

- Python 3.11+
- Docker
- Kubernetes cluster such as Docker Desktop Kubernetes, `minikube`, or `kind`

## Run Locally

Install dependencies:

```bash
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements.txt -r requirements-dev.txt
```

Start the API:

```bash
.venv/bin/uvicorn main:app --host 0.0.0.0 --port 8080
```

Open:

- `http://localhost:8080/health`
- `http://localhost:8080/docs`

## API Examples

Health check:

```bash
curl http://localhost:8080/health
```

Example analyze request:

```bash
curl -X POST http://localhost:8080/api/analyze \
  -H "Content-Type: application/json" \
  -d '{"text":"oats with sugar and salt"}'
```

Example response:

```json
{
  "assessments": {
    "Sugar": {
      "rating": "unhealthy",
      "reason": "High added sugar is usually treated as a less healthy ingredient."
    },
    "Oats": {
      "rating": "healthy",
      "reason": "Oats are commonly treated as a fiber-rich whole grain ingredient."
    },
    "Salt": {
      "rating": "neutral",
      "reason": "Salt is not automatically bad, but intake depends on quantity and context."
    }
  }
}
```

## Docker

Build the image:

```bash
docker build -t learning-backend:local .
```

Run the container:

```bash
docker run --rm -p 8080:8080 learning-backend:local
```

The container runs the app with:

```bash
uvicorn main:app --host 0.0.0.0 --port 8080
```

## Kubernetes

Kubernetes manifests are kept separately under `../infrastructure/k8s/`.

- `deployment.yaml` creates a Deployment named `learning-backend`
- the Deployment runs `2` replicas
- the container image is `learning-backend:local`
- the app listens on container port `8080`
- `service.yaml` exposes the app on Service port `80` and forwards to `8080`

Apply the manifests:

```bash
kubectl apply -f ../infrastructure/k8s/deployment.yaml
kubectl apply -f ../infrastructure/k8s/service.yaml
```

Check resources:

```bash
kubectl get deployments
kubectl get pods
kubectl get services
```

## Notes

- This backend returns mocked results for learning purposes.
- If you use a local Kubernetes cluster, make sure the cluster can access the `learning-backend:local` image, or load/push the image appropriately for your environment.
