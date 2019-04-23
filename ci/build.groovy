import groovy.json.JsonOutput

node {
    try {
        def packagename = "jupyter-html-converter"
        def targetBucket = "accedia-jupyter-lambda-source"
        def downloadBucketValue = "accedia-jupyter-notebooks"
        def uploadBucketValue = "accedia-jupyter-html"
        def pythonPathValue = "/var/task"
        def ipythonDirValue = "/tmp/ipythondir"
        def preprocessorTimeoutInSeconds = '600'

        def envVariables = JsonOutput.toJson([
            Variables: [
                download_bucket: downloadBucketValue,
                upload_bucket: uploadBucketValue,
                PYTHONPATH: pythonPathValue,
                IPYTHONDIR: ipythonDirValue,
                preprocessor_timeout_in_seconds: preprocessorTimeoutInSeconds
            ]
        ])

        stage('Prepare') {
            cleanWs()
            def scmVars = checkout scm
            commitHash = scmVars.GIT_COMMIT
            buildImage = docker.build("build-${packagename}", "-f ci/Dockerfile .")
        }

        stage('Build') {
            buildImage.inside() {
                sh "cd ci && chmod +x *.sh"
                sh "cd ci && bash ./build_lambda.sh"
            }
        }

        stage('Deploy') {
            sh "aws s3 cp dist/function.zip s3://${targetBucket}/function-${commitHash}.zip"
            sh "aws lambda update-function-code --function-name ${packagename} --s3-bucket ${targetBucket} --s3-key function-${commitHash}.zip"
            sh "aws lambda update-function-configuration --function-name ${packagename} --environment '${envVariables}'"
        }
    }
    finally {
        step([$class: 'Mailer', notifyEveryUnstableBuild: true, recipients: emailextrecipients([[$class: 'CulpritsRecipientProvider'], [$class: 'RequesterRecipientProvider']])])
    }
}
