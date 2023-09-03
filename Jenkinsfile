
pipeline {
    agent any
    
    stages {
        
        stage('Run Python Script') {
            steps {
                script {
                    // Define the Python command to run your script
                    def pythonCmd = 'python3 memory_usage.py ${username} ${password} ${csvpath} ${reportpath}'
                    
                    // Run the Python script
                    sh returnStatus: true, script: pythonCmd
                }
            }
        }
    }
    
    post {
        success {
            echo 'The Python script executed successfully.'
        }
        failure {
            echo 'The Python script failed to execute.'
        }
    }
}
