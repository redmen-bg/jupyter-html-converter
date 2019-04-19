import os
from aws import download_from_s3_bucket, upload_to_s3_bucket
from notebooks import convert_to_html
from files import create_temp_file, delete_temp_files, write_to_file

DOWNLOAD_BUCKET = os.environ['download_bucket']
UPLOAD_BUCKET = os.environ['upload_bucket']

def handler(event, context):
    notebook_name = event['notebook_name']
    notebook_file = create_temp_file()
    download_from_s3_bucket(DOWNLOAD_BUCKET, notebook_name, notebook_file)

    notebook_html = convert_to_html(notebook_file)

    notebook_html_file = create_temp_file()
    write_to_file(notebook_html, notebook_html_file)

    notebook_html_name = notebook_name.split(".")[0] + ".html"
    upload_to_s3_bucket(notebook_html_file, UPLOAD_BUCKET, notebook_html_name)

    delete_temp_files(notebook_file, notebook_html_file)