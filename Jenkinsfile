pipeline {
    agent any

    environment {
        IMAGE_NAME = 'technova-inventory'
        DOCKERHUB_REPO = 'aartik1704/technova-inventory'
    }

    stages {
        stage('Clone Code') {
            steps {
                git branch: 'main', url: 'https://github.com/aartik17/technova-inventory-app1.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t $IMAGE_NAME .'
            }
        }

        stage('Login to Docker Hub') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'DockerHub', usernameVariable: 'USERNAME', passwordVariable: 'PASSWORD')]) {
                    sh 'echo $PASSWORD | docker login -u $USERNAME --password-stdin'
                }
            }
        }

        stage('Push to Docker Hub') {
            steps {
                sh '''
                    docker tag $IMAGE_NAME $DOCKERHUB_REPO
                    docker push $DOCKERHUB_REPO
                '''
            }
        }

        stage('Deploy Container') {
            steps {
                sh '''
                    docker stop $IMAGE_NAME || true
                    docker rm $IMAGE_NAME || true
                    docker run -d -p 5000:5000 --name $IMAGE_NAME $DOCKERHUB_REPO
                '''
            }
        }
    }
}
