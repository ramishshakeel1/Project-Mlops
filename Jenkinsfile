pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git credentialsId: 'github-pat', branch: 'dev', url: 'https://github.com/Shaheer-Haq/Project_MLOps.git'
            }
        }

        stage('Pull Docker Image') {
            steps {
                script {
                    docker.pull('shaheerhaq/mlops-pipeline')
                }
            }
        }
    }
}