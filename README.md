**Deployment Instructions**

**Local Environment**

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

1.Build and push the Docker image:

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

**CI/CD Pipeline Setup**

1.Configure Jenkins with the provided Jenkinsfile.
2.Ensure credentials for Docker and Kubernetes are set.
3.Trigger the pipeline to build, test, and deploy the application.

**Logging and Monitoring Setup**

1.Enable kubectl logs for pod monitoring:
  kubectl logs -f <pod-name> -n v1
2.Set up Prometheus & Grafana for advanced monitoring.
3.Apply custom alerts based on CPU/memory thresholds.

**SYSTEM_DESIGN.md**

**Architectural Overview**

The Product Catalog Microservice is a containerized application designed for scalability and maintainability. It is deployed on Kubernetes with namespace isolation, resource constraints, and CI/CD automation.

**key Design Decisions**

1.Containerization: Uses Docker for consistent deployment.
2.Versioning Strategy: Each version is deployed in a separate namespace.
3.Scalability: Horizontal Pod Autoscaler (HPA) manages scaling.
4.Ingress Routing: NGINX routes traffic based on version (/v1, /v1.1, /v2).
5.Monitoring: Integrated with Prometheus & Grafana for performance insights.





















