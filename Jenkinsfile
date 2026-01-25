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

         echo "=== Arduino CLI ==="
         arduino-cli version

         echo "=== Update index & ensure AVR core ==="
         arduino-cli core update-index
         arduino-cli core list | grep -q '^arduino:avr' || arduino-cli core install arduino:avr

         echo "=== Detect board port ==="
         PORT=$(arduino-cli board list | awk 'NR>1 && $1 ~ /^\\/dev\\// {print $1; exit}')
         echo "Detected port: $PORT"
         test -n "$PORT"

         echo "=== Compile ==="
         arduino-cli compile --fqbn "$FQBN" blink

         echo "=== Upload ==="
         arduino-cli upload -p "$PORT" --fqbn "$FQBN" blink

         echo "=== DONE ==="
        '''
      }
    }
  }
}
