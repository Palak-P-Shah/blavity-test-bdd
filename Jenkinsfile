pipeline {
    
    stages {
        stage('Build') { 
            
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