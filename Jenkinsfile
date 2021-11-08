pipeline {
    agent { Dockerfile true }
    stages 
    {
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