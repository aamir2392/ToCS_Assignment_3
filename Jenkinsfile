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
                gcloud compute scp /var/lib/jenkins/caches/git-c4874a9e3c7908b5172c62281e5beb2a/index.html root@apache-server:/var/www/html --zone=us-central1-a
                '''
            }
        }
    }
}
