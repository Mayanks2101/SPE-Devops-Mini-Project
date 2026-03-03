pipeline {
    agent any

    environment {
        DOCKER_REPO = "mayank2101/spe-miniproject-calculator"
        GIT_REPO = "https://github.com/Mayanks2101/SPE-Devops-Mini-Project.git"
        GIT_BRANCH = "main"
        IMAGE_TAG = "${BUILD_NUMBER}"
    }

    stages {

        stage('Checkout') {
            steps {
                git branch: "${GIT_BRANCH}", url: "${GIT_REPO}"
            }
        }

        stage('Install Dependencies') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                sh 'pytest'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh '''
                    docker build -t $DOCKER_REPO:$IMAGE_TAG .
                    docker tag $DOCKER_REPO:$IMAGE_TAG $DOCKER_REPO:latest
                '''
            }
        }

        stage('Push Docker Image') {
            steps {
                withCredentials([usernamePassword(
                    credentialsId: 'dockerhub-creds',
                    usernameVariable: 'USERNAME',
                    passwordVariable: 'PASSWORD'
                )]) {
                    sh '''
                        echo $PASSWORD | docker login -u $USERNAME --password-stdin
                        docker push $DOCKER_REPO:$IMAGE_TAG
                        docker push $DOCKER_REPO:latest
                    '''
                }
            }
        }
    }

    post {
        success {
            emailext(
                subject: "SUCCESS: ${env.JOB_NAME} #${env.BUILD_NUMBER}",
                body: """
                Build was successful!

                Image pushed:
                $DOCKER_REPO:$IMAGE_TAG

                Check details at:
                ${env.BUILD_URL}
                """,
                recipientProviders: [developers()]
            )
        }

        failure {
            emailext(
                subject: "FAILED: ${env.JOB_NAME} #${env.BUILD_NUMBER}",
                body: """
                Build failed!

                Project: ${env.JOB_NAME} #${env.BUILD_NUMBER}
                Check logs:
                ${env.BUILD_URL}
                """,
                recipientProviders: [developers()]
            )
        }
    }
}