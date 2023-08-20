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
        stage('Build and push docker image') {
            def customImage = docker.build("app-image:$env.BUILD_ID")
            customImage.push()
        }
    }
}
