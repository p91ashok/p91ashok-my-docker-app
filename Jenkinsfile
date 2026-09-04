// pipeline {
//     agent {
//         label 'app'
//     }

//     stages {

//         stage('Checkout') {
//             steps {
//                 echo 'Source code checked out from GitHub'
//                 sh 'git log -1 --oneline'
//             }
//         }

//         stage('Test') {
//             steps {
//                 echo 'Running Python syntax check'
//                 sh 'python3 -m py_compile app.py'
//             }
//         }

//         stage('Docker Build') {
//             steps {
//                 echo 'Building Docker image'
//                 sh 'docker build -t devops-demo:${BUILD_NUMBER} .'
//             }
//         }

//         stage('Docker Run') {
//             steps {
//                 echo 'Starting test container'

//                 sh '''
//                     docker rm -f devops-demo-test 2>/dev/null || true

//                     docker run -d \
//                         --name devops-demo-test \
//                         -p 5000:5000 \
//                         devops-demo:${BUILD_NUMBER}

//                     sleep 5

//                     curl -f http://localhost:5000/health
//                 '''
//             }
//         }
//     }

//     post {
//         always {
//             echo 'Cleaning up test container'

//             sh '''
//                 docker rm -f devops-demo-test 2>/dev/null || true
//             '''
//         }

//         success {
//             echo '========================================'
//             echo 'PIPELINE COMPLETED SUCCESSFULLY'
//             echo '========================================'
//         }

//         failure {
//             echo '========================================'
//             echo 'PIPELINE FAILED'
//             echo '========================================'
//         }
//     }
// }



pipeline {
    agent {
        label 'app'
    }

    stages {

        stage('Checkout') {
            steps {
                echo '========================================'
                echo 'CHECKOUT'
                echo '========================================'

                echo 'Source code checked out from GitHub'
                sh 'git log -1 --oneline'
                sh 'ls -la'
            }
        }

        stage('Test') {
            steps {
                echo '========================================'
                echo 'PYTHON TEST'
                echo '========================================'

                echo 'Running Python syntax check'

                sh '''
                    python3 -m py_compile app.py
                '''
            }
        }

        stage('Docker Build') {
            steps {
                echo '========================================'
                echo 'DOCKER BUILD'
                echo '========================================'

                echo "Building Docker image: devops-demo:${BUILD_NUMBER}"

                sh '''
                    docker build \
                        -t devops-demo:${BUILD_NUMBER} \
                        -t devops-demo:latest \
                        .
                '''

                sh '''
                    docker images | grep devops-demo
                '''
            }
        }

        stage('Stop Old Container') {
            steps {
                echo '========================================'
                echo 'STOP OLD CONTAINER'
                echo '========================================'

                sh '''
                    docker rm -f devops-demo 2>/dev/null || true
                '''
            }
        }

        stage('Deploy Container') {
            steps {
                echo '========================================'
                echo 'DEPLOY CONTAINER'
                echo '========================================'

                sh '''
                    docker run -d \
                        --name devops-demo \
                        --restart unless-stopped \
                        -p 5000:5000 \
                        devops-demo:${BUILD_NUMBER}
                '''
            }
        }

        stage('Health Check') {
            steps {
                echo '========================================'
                echo 'HEALTH CHECK'
                echo '========================================'

                sh '''
                    echo "Waiting for application to start..."
                    sleep 5

                    echo "Checking application health..."
                    curl -f http://localhost:5000/health
                '''
            }
        }

        stage('Verify Deployment') {
            steps {
                echo '========================================'
                echo 'VERIFY DEPLOYMENT'
                echo '========================================'

                sh '''
                    echo "Running containers:"
                    docker ps

                    echo ""
                    echo "Application container:"
                    docker ps --filter "name=devops-demo"

                    echo ""
                    echo "Container logs:"
                    docker logs --tail 20 devops-demo
                '''
            }
        }
    }

    post {

        success {
            echo '''
========================================
PIPELINE COMPLETED SUCCESSFULLY
========================================
Application deployed successfully.

Container:
    devops-demo

Port:
    5000

Image:
    devops-demo:${BUILD_NUMBER}

Health:
    http://localhost:5000/health
========================================
'''
        }

        failure {
            echo '''
========================================
PIPELINE FAILED
========================================
Please check the Jenkins console output.
========================================
'''
            
            sh '''
                echo "Docker containers:"
                docker ps -a

                echo ""
                echo "Docker logs:"
                docker logs --tail 50 devops-demo 2>/dev/null || true
            '''
        }
    }
}