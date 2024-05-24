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
                gcloud compute scp /var/lib/jenkins/workspace/multiPipeline_main/index.html root@apache-server:/var/www/html --zone=us-central1-a
                '''
            }
        }
    }
}
