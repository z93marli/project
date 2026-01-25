pipeline {
  agent { label 'rpi' }
  stages {
    stage('Checkout') {
      steps {
        git branch: 'main', url: 'https://github.com/z93marli/project.git'
      }
    }
    stage('Build') {
      steps {
        sh '''
          set -eux
          pwd
          ls -la
        '''
      }
    }
  }
}
