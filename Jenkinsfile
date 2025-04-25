pipeline {
    agent any

    stages {
        stage('Clone') {
            steps {
                git 'https://github.com/Priyank-Jain-254/Book_store.git'
            }
        }

        stage('Build') {
            steps {
                sh 'docker-compose build'
            }
        }

        stage('Run Tests') {
            steps {
                sh 'python manage.py test'
            }
        }

        stage('Deploy') {
            steps {
                sh 'docker-compose up -d'
            }
        }
    }
}
