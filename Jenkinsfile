pipeline {
  agent { label 'rpi' }

  environment {
    FQBN = 'arduino:avr:uno'   // Ändra om du har Nano etc
    SKETCH_DIR = '.'          // Ändra om .ino ligger i en mapp
  }

  stages {
    stage('Checkout') {
      steps {
        git branch: 'main', url: 'https://github.com/z93marli/project.git'
      }
    }

    stage('Compile Arduino Sketch') {
      steps {
        sh '''
          set -eux
          echo "Workspace:"
          pwd
          ls -la

          arduino-cli version
          arduino-cli core update-index
          arduino-cli compile --fqbn "$FQBN" ./blink.ino
        '''
      }
    }
  }
}
