import os
import nbformat
from nbconvert import HTMLExporter
import boto3


s3_client = boto3.client('s3')

def handler(event, context):
    DOWNLOAD_PATH = os.environ['download_path']
    UPLOAD_PATH = os.environ['upload_path']
    DOWNLOAD_BUCKET = os.environ['download_bucket']
    UPLOAD_BUCKET = os.environ['upload_bucket']

    NOTEBOOK_NAME = event['notebook_name']
    HTML_NAME = NOTEBOOK_NAME.split(".")[0] + ".html"

    s3_client.download_file(DOWNLOAD_BUCKET, NOTEBOOK_NAME, DOWNLOAD_PATH)

    # print("Attempt to download the notebook to %s" % DOWNLOAD_PATH)

    with(open(DOWNLOAD_PATH, "r")) as notebook_file:
        notebook_data = notebook_file.read()

    # print("Attempt to read the notebook from %s" %  DOWNLOAD_PATH)
        notebook = nbformat.reads(notebook_data, as_version=4)

        # print("Attempt to convert the notebook from %s" % DOWNLOAD_PATH)

        html_exporter = HTMLExporter()
        html_exporter.template_file = 'basic'

        (body, resources) = html_exporter.from_notebook_node(notebook)

    # print("Attempt to write the converted notebook to %s" % UPLOAD_PATH)

    with(open(UPLOAD_PATH, "w")) as html_file:
        html_file.write(body)

    # print("Attempt to upload the converted notebook from %s" % UPLOAD_PATH)

        s3_client.upload_file(UPLOAD_PATH, UPLOAD_BUCKET, HTML_NAME)




     

