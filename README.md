# Deployment Instructions

## Local Environment Setup

<<<<<<< HEAD

1.Clone the repository:
  git clone <repo-url>
  cd Task-2
2.Create and activate a virtual environment:
  python -m venv venv
  source venv/bin/activate  # On Windows: venv\Scripts\activate
3.Install dependencies:
  pip install -r requirements.txt
4.Run the application:
  python app.py  # Adjust for v1.0, v1.1, or v2.0
  
**Kubernetes Deployment**
=======
| Step | Command |
|------|---------|
| **1. Clone the repository** | `git clone https://github.com/Bharathimula/Task-2.git` <br> `cd Task-2` |
| **2. Create & activate virtual environment** (Linux/macOS) | `python -m venv venv` <br> `source venv/bin/activate` |
| **2. Create & activate virtual environment** (Windows) | `python -m venv venv` <br> `venv\Scripts\activate` |
| **3. Install dependencies** | `pip install -r requirements.txt` |
| **4. Run the application** | `python app.py` (for v1.0, v1.1, or v2.0) |
>>>>>>> 932438d (Updated README with structured Deployment & Monitoring details)


# Kubernetes Deployment

## 1. Build and Push the Docker Image
```sh
docker build -t myrepo/product-catalog:v1 .
docker push myrepo/product-catalog:v1

Repeat for other versions.

2.Apply Kubernetes manifests:

kubectl apply -f deployment-v1.yml
kubectl apply -f hpa.yml
kubectl apply -f ingress.yml

3.Verify deployment:

kubectl get pods -n v1
kubectl get services -n v1
kubectl get ingress -n v1

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

2.Set up Prometheus & Grafana for advanced monitoring.
3.Apply custom alerts based on CPU/memory thresholds.


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







