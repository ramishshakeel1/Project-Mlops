pipeline {
    agent any

    environment {
        DOCKERHUB_CREDENTIALS = credentials('dockerhub-credentials') 
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
                script {
                    docker.build("${DOCKERHUB_REPO}")
                }
            }
        }

        stage('Push to Docker Hub') {
            steps {
                script {
                    docker.withRegistry('https://index.docker.io/v1/', 'dockerhub-credentials') {
                        docker.image("${DOCKERHUB_REPO}").push('latest')
                    }
                }
            }
        }
    }
}
