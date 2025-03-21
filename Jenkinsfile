pipeline {
    agent any

    environment {
        DOCKER_IMAGE = "bharu2703/product-catalog:${env.BUILD_ID}"
    }

    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/Bharathimula/Task-2/product-catalog.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t $DOCKER_IMAGE .'
            }
        }

        stage('Push Image to Docker Hub') {
            steps {
                withDockerRegistry([credentialsId: 'docker-hub-credentials', url: '']) {
                    sh 'docker push $DOCKER_IMAGE'
                }
            }
        }

        stage('Deploy to Kubernetes') {
            steps {
                sh 'kubectl set image deployment/product-catalog product-catalog=$DOCKER_IMAGE'
                sh 'kubectl rollout status deployment/product-catalog'
            }
        }

        stage('Run Tests') {
            steps {
                sh 'curl --fail http://your-k8s-service-url/health'
                sh 'curl --fail http://your-k8s-service-url/products'
            }
        }
    }
}

