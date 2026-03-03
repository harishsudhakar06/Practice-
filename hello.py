print("my first git process")
print("hello jenkins")
#pipeline {
    #agent any

    parameters {
        string(name: 'MESSAGE', defaultValue: 'Hello')
    }

    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/username/repo.git'
            }
        }

        stage('Print Parameter') {
            steps {
                echo "Message: ${params.MESSAGE}"
            }
        }

        stage('BAT Command') {
            steps {
                bat 'echo Hello from Jenkins'
            }
        }
    }
}
