pipeline {
    agent {
        docker {
            image 'docker:latest'               // Use Docker image with Docker CLI
            args '-v /var/run/docker.sock:/var/run/docker.sock'  // Mount host Docker socket
        }
    }

    environment {
        DOCKERHUB_CREDENTIALS = credentials('dockerhub-credentials') // Replace with your DockerHub ID
    }

    stages {
        stage('Checkout') {
            steps {
                git branch: 'dev', url: 'https://github.com/ramishshakeel1/Project-Mlops.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t 21i1363/mlops-pipeline:latest .'
            }
        }

        stage('Push to Docker Hub') {
            steps {
                sh """
                echo "$DOCKERHUB_CREDENTIALS_PSW" | docker login -u "$DOCKERHUB_CREDENTIALS_USR" --password-stdin
                docker push 21i1363/mlops-pipeline:latest
                """
            }
        }
    }
}
