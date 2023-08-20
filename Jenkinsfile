pipeline {
    agent any

    environment {

        registryCredential = 'dockerhub'
    }
 
    stages {

        stage('Fetch code'){
            steps {
                git branch: 'main', url: 'https://github.com/RetupmocDren/cicd.git'
            }
        }
        
        stage('Build app') {
            steps {
                sh "python3 app.py 'Solar System'"
            }
        }
        
        stage('Test app') {
            steps {
                sh "python3 test.py"
            }
        }
        
        stage('Build docker image') {
            steps {
                sh "docker build -t 'app-image:${env.BUILD_ID}' ."
            }
        }
        stage('Push docker image') {
            steps {
                sh "docker push 'retupmocdren/app-image:${env.BUILD_ID}'"
            }
        }
    }
}
