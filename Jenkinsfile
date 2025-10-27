pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                // Pull your latest code from GitHub
                git branch: 'main', url: 'https://github.com/shivagopaluni9966/sivanewproj.git'
            }
        }

        stage('Build') {
            steps {
                echo 'Building Flask application...'
                sh 'python3 -m py_compile app.py'
            }
        }

        stage('Test') {
            steps {
                echo 'Running tests...'
                // Optional: Add test command if you have any test scripts
            }
        }

        stage('Deploy') {
            steps {
                echo 'Deploy stage (placeholder)...'
                // Add docker build or deployment commands here later
            }
        }
    }
}
