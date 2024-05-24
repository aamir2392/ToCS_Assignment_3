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
                sh "python3 sample.py"
                sh '''
                gcloud compute scp /var/lib/jenkins/workspace/Jenkins-GDC-Demo_main/index.html root@appserver:/var/www/html --zone=us-west4-b
                '''
            }
        }
    }
}
