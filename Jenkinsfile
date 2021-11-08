pipeline {
    agent any
    stages 
    {
	stage("build docker image") 
	{
            agent 
	    {
                docker { image 'python:3.5.1' }
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