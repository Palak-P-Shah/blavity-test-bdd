pipeline {
    agent none
    stages {
        stage('Build') { 
            agent { docker 'dcc6955756f5' }
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