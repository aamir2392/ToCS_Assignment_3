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
                sh '''
                gcloud compute scp /var/lib/jenkins/workspace/multiPipeline_main/ root@apache-server:/var/www/html --zone=us-central1-a
                '''
            }
        }
    }
}
