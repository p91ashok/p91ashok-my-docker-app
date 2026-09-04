pipeline {
    agent {
        label 'app'
    }

    stages {

        stage('Checkout') {
            steps {
                echo 'Source code checked out from GitHub'
                sh 'git log -1 --oneline'
            }
        }

        stage('Test') {
            steps {
                echo 'Running Python syntax check'
                sh 'python3 -m py_compile app.py'
            }
        }

        stage('Docker Build') {
            steps {
                echo 'Building Docker image'
                sh 'docker build -t devops-demo:${BUILD_NUMBER} .'
            }
        }

        stage('Docker Run') {
            steps {
                echo 'Starting test container'

                sh '''
                    docker rm -f devops-demo-test 2>/dev/null || true

                    docker run -d \
                        --name devops-demo-test \
                        -p 5000:5000 \
                        devops-demo:${BUILD_NUMBER}

                    sleep 5

                    curl -f http://localhost:5000/health
                '''
            }
        }
    }

    post {
        always {
            echo 'Cleaning up test container'

            sh '''
                docker rm -f devops-demo-test 2>/dev/null || true
            '''
        }

        success {
            echo '========================================'
            echo 'PIPELINE COMPLETED SUCCESSFULLY'
            echo '========================================'
        }

        failure {
            echo '========================================'
            echo 'PIPELINE FAILED'
            echo '========================================'
        }
    }
}