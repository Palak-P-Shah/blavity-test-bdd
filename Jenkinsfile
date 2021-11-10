pipeline {
    agent none
    stages {
        stage('Build') { 
            agent { docker 'python3' }
            steps {
                sh 'python --version'
		sh 'pip --version'
		sh 'pip install selenium'
		sh 'pip install behave'
		sh 'pip install webdriver-manager'
		sh 'behave ./GUIAutomatedTests/features/opinion.feature'
            }
        }
    }
}