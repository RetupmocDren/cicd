pipeline {
    agent any

    stages {
        stage('Build'){
            steps {
                step {
                    sh python app.py "Solar System"
                }
            }
        }
    }
}