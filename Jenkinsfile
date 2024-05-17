pipeline {
    agent any
    
    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        stage('Build') {
            steps {
                sh 'echo Building the application'
          #      sh 'python sample.py'
            }
        }
    }
}
