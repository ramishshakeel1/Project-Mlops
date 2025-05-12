pipeline {
    agent any

    environment {
        DOCKERHUB_REPO = '21i1363/mlops-pipeline'
    }

    stages {
        stage('Checkout') {
            steps {
                git branch: 'dev', credentialsId: 'github-pat', url: 'https://github.com/ramishshakeel1/Project-Mlops.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh "docker build -t ${DOCKERHUB_REPO}:latest ."
            }
        }

        stage('Push to Docker Hub') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'dockerhub-credentials', usernameVariable: 'DOCKER_USER', passwordVariable: 'DOCKER_PASS')]) {
                    sh """
                        echo "$DOCKER_PASS" | docker login -u "$DOCKER_USER" --password-stdin
                        docker push ${DOCKERHUB_REPO}:latest
                    """
                }
            }
        }
    }
}
