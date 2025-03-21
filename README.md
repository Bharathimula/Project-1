# Deployment Instructions

## Local Environment Setup

1. Clone the repository:

   ```sh
   git clone <repo-url>
   cd Task-2
   ```

2. Create and activate a virtual environment:

   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:

   ```sh
   pip install -r requirements.txt
   ```

4. Run the application:

   ```sh
   python app.py  # Adjust for v1.0, v1.1, or v2.0
   ```

## Kubernetes Deployment

1. Clone the repository:

   ```sh
   git clone https://github.com/Bharathimula/Task-2.git
   cd Task-2
   ```

2. Install dependencies:

   ```sh
   pip install -r requirements.txt
   ```

3. Run the application:

   ```sh
   python app.py  # Adjust for v1.0, v1.1, or v2.0
   ```

## 1. Build and Push the Docker Image

```sh

docker build -t myrepo/product-catalog:v1.0 .
docker push myrepo/product-catalog:v1.0

docker build -t myrepo/product-catalog:v1.1 .
docker push myrepo/product-catalog:v1.1

docker build -t myrepo/product-catalog:v2.0 .
docker push myrepo/product-catalog:v2.0
```

## 2. Apply Kubernetes Manifests

```sh
kubectl apply -f deployment-v1.yml
kubectl apply -f hpa.yml
kubectl apply -f ingress.yml
```

## 3. Verify Deployment

```sh
kubectl get pods -n v1
kubectl get services -n v1
kubectl get ingress -n v1
```

# CI/CD Pipeline Setup

## 1. Configure Jenkins
- Set up Jenkins with the provided `Jenkinsfile`.

## 2. Set Credentials
- Ensure credentials for Docker and Kubernetes are configured in Jenkins.

## 3. Trigger the Pipeline
- Run the pipeline to **build, test, and deploy** the application.

# Monitoring & Logging Setup

## 1. Enable Pod Monitoring with `kubectl logs`

```sh
kubectl logs -f <pod-name> -n v1
```

2. Set up **Prometheus & Grafana** for advanced monitoring.
3. Apply custom alerts based on CPU/memory thresholds.

# System Design

## **Architectural Overview**

The **Product Catalog Microservice** is a **containerized** application designed for **scalability** and **maintainability**. It is deployed on **Kubernetes** with:
- **Namespace isolation**
- **Resource constraints**
- **CI/CD automation**

## **Key Design Decisions**

1. **Containerization**: Uses **Docker** for consistent deployment.  
2. **Versioning Strategy**: Each version is deployed in a **separate namespace**.  
3. **Scalability**: Uses **Horizontal Pod Autoscaler (HPA)** for dynamic scaling.  
4. **Ingress Routing**: Uses **NGINX** to route traffic based on version (`/v1`, `/v1.1`, `/v2`).  
5. **Monitoring**: Integrated with **Prometheus & Grafana** for performance insights.  

# Documentation

- **README.md**
  - Deployment instructions for local and Kubernetes environments.
  - CI/CD pipeline setup and execution steps.
  - Logging and monitoring setup guide.

- **SYSTEM_DESIGN.md**
  - Detailed explanation of architectural decisions.
