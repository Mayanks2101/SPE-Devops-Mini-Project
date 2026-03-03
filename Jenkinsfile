pipeline {
    agent any

    environment {
        DOCKER_IMAGE = "mayank2101/spe-miniproject-calculator:latest"
        GIT_REPO = "https://github.com/Mayanks2101/SPE-Devops-Mini-Project.git"
        GIT_BRANCH = "main"
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
                sh 'docker build -t $DOCKER_IMAGE .'
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
                        docker push $DOCKER_IMAGE
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

                Project: ${env.JOB_NAME}
                Check details at: ${env.BUILD_URL}
                """,
                recipientProviders: [developers()]
            )
        }

        failure {
            emailext(
                subject: "FAILED: ${env.JOB_NAME} #${env.BUILD_NUMBER}",
                body: """
                Build failed!

                Project: ${env.JOB_NAME}
                Check details at: ${env.BUILD_URL}
                """,
                recipientProviders: [developers()]
            )
        }
    }
}