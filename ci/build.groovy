node {
    try {
        def packagename = "jupyter-html-converter"
        def targetBucket = "accedia-jupyter-lambda-source"

        stage('Prepare') {
            cleanWs()
            def scmVars = checkout scm
            commitHash = scmVars.GIT_COMMIT
            buildImage = docker.build("build-${packagename}", "-f ci/Dockerfile .")
        }

        stage('Build') {
            buildImage.inside() {
                sh "cd ci && chmod +x *.sh"
                sh "cd ci && sh ./build_lambda.sh"
            }
        }

        stage('Deploy') {
            sh "aws s3 cp dist/function.zip s3://${targetBucket}/function-${commitHash}.zip"
            sh "aws lambda update-function-code --function-name ${packagename} --s3-bucket ${targetBucket} --s3-key function-${commitHash}.zip"
        }
    }
    finally {
        step([$class: 'Mailer', notifyEveryUnstableBuild: true, recipients: emailextrecipients([[$class: 'CulpritsRecipientProvider'], [$class: 'RequesterRecipientProvider']])])
    }
}
