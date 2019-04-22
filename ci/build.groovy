node {
    try {
        // Configuration
        def packagename = "jupyter-html-converter"

        stage('Prepare') {
            deleteDir()
            checkout scm
        }

    }
    finally {
        step([$class: 'Mailer', notifyEveryUnstableBuild: true, recipients: emailextrecipients([[$class: 'CulpritsRecipientProvider'], [$class: 'RequesterRecipientProvider']])])
    }
}
