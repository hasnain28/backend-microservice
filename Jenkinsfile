pipeline {
  agent any
  environment {
		registryCredential = 'dockerhub'
	}
  stages {
    stage('Build') {
			steps {
				dir('backend'){
					sh 'docker build -t hasnainzaib/abc .'
				}
			}
		}
    stage('Test') {
      steps {
			dir('backend'){
				sh 'docker container run --rm -p 8097:8080 --name node -d hasnainzaib/abc'
				sh 'sleep 15'
// 				sh 'curl -I http://localhost:8097'
			}
		}
	}
    stage('Publish') {
			steps{
				script {
					docker.withRegistry( '', registryCredential ) {
						sh 'docker push hasnainzaib/abc'
					}
				}
			}
		}
	}
}