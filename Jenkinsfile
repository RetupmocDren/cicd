pipeline {
    agent any
    stages {
        stage('Fetch code'){
            steps {
                git branch: 'main', url: 'https://github.com/RetupmocDren/cicd.git'
            }
        }
        stage('Build') {
            steps {
                sh "python3 app.py 'olar System'"
            }
        }
        stage('Test') {
            steps {
                sh "python3 test.py"
            }
        }
    }
}
