pipeline {
	
    stages 
    {
	stage('Initialize')
	{
	    steps
	    {
        	def dockerHome = tool 'test-docker'
        	env.PATH = "${dockerHome}/bin:${env.PATH}"
	    }
    	}
    	agent { docker { image 'python:3.5.1' } }
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