# Learning Backend

This repository is the local learning track for the backend application.

It is intentionally organized into two main areas so the difference between application work and deployment work is explicit.

## Repository Structure

```text
.
|-- .github/
|   `-- workflows/
|       `-- test.yml
|-- app/
|   |-- Dockerfile
|   |-- README.md
|   |-- main.py
|   |-- requirements-dev.txt
|   |-- requirements.txt
|   `-- tests/
|       `-- test_main.py
|-- infrastructure/
|   `-- k8s/
|       |-- deployment.yaml
|       `-- service.yaml
`-- README.md
```

## What Each Area Means

### `app/`

This directory contains the application and image-build concerns:

- FastAPI source code
- Python dependency files
- tests
- Dockerfile
- app-specific README

This is the part that answers:

- what the application does
- how the application is tested
- how the application image is built

### `infrastructure/`

This directory contains deployment configuration concerns:

- Kubernetes manifests
- later, this can also contain Argo CD or other deployment-related definitions

This is the part that answers:

- where the application runs
- how Kubernetes should deploy it
- what desired state should exist in the cluster

### `.github/workflows/`

This directory contains pipeline orchestration for the whole repository.

The workflow lives at repo level because it coordinates both:

- application steps such as test and image build
- infrastructure/deployment steps such as applying manifests

## Current Workflow Model

The current pipeline stages are:

1. `test`
2. `build-image`
3. `deploy`

Current intent:

- `test` validates the app in `app/`
- `build-image` builds the Docker image from `app/`
- `deploy` applies Kubernetes configuration from `infrastructure/`

## Notes

- For local learning, `minikube` is still the active cluster path.
- The `deploy` stage is environment-coupled to the local host setup.
- The app/deployment split is mainly for learning clarity and GitOps-style reasoning.

## Where To Read Next

- start with [app/README.md](/Users/talllam/Documents/docker-kubernetes/learning-backend/app/README.md) for app-specific details
- use [.github/workflows/test.yml](/Users/talllam/Documents/docker-kubernetes/learning-backend/.github/workflows/test.yml) for pipeline learning
- use [infrastructure/k8s/deployment.yaml](/Users/talllam/Documents/docker-kubernetes/learning-backend/infrastructure/k8s/deployment.yaml) and [service.yaml](/Users/talllam/Documents/docker-kubernetes/learning-backend/infrastructure/k8s/service.yaml) for Kubernetes deployment learning
