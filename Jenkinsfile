pipeline {
	
    stages 
    {
	stage("build docker image") 
	{
            when {
                expression {
                    script {
                       env.BRANCH_NAME.toString().equals('main') && CODE_CHANGES == false
                    }
                }
            }
            steps {
                sh "docker build -t ${python:3.5.1} ."
            }
        }
        stage('build') 
	{
            steps 
	    {
                sh 'python --version'
            }
        }
	stage('install dependencies') 
	{
            steps 
	    {
                sh 'pip install behave'
		sh 'pip install selenium'
		sh 'pip install webdriver-manager'
            }
        }
	stage('test') 
	{
            steps 
	    {
                sh 'behave ./GUIAutomatedTests/features/Homepage.feature'
            }
        }
    }
}