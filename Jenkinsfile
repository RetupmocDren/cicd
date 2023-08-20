pipeline {
    agent any

    environment {
        registry = ""
        registryCredential = 'dockerhub'
    }

    stages {
        stage('Fetch code'){
            steps {
                git branch: 'main', url: 'https://github.com/RetupmocDren/cicd.git'
            }
        }
        stage('Build') {
            steps {
                sh "python3 app.py 'Solar System'"
            }
        }
        stage('Test') {
            steps {
                sh "python3 test.py"
            }
        }
        stage('Push artifacts') {
            
        }
        stage('Build docker image') {

        }
    }
}
