pipeline {
    agent { docker { image 'python:3.5.1' } }
    stages 
    {
        stage('build') 
	{
            steps 
	    {
                sh 'python --version'
            }
        }
	stage('install') 
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