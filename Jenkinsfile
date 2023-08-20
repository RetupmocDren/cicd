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
                python3 app.py "Solar System"
            }
        }
        stage('Test') {
            steps {
                python3 test.py
            }
        }
    }
}
