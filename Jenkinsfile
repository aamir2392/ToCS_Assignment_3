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
                gcloud compute ssh root@apache-server --zone=us-central1-a -- "rm -rf /var/www/html/*"
                gcloud compute scp --recurse /var/lib/jenkins/workspace/multiPipeline_main/ root@apache-server:/var/www/html --zone=us-central1-a
                '''
            }
        }
    }
}
