import os
from aws import download_from_s3_bucket, upload_to_s3_bucket
from notebooks import convert_to_html_file
from files import create_temp_file, delete_temp_files, write_to_file

DOWNLOAD_BUCKET = os.environ['download_bucket']
UPLOAD_BUCKET = os.environ['upload_bucket']

def handler(event, context):

    import subprocess
    print("----------------- pwd:")
    subprocess.run(["pwd"])
    print("----------------- ls")
    subprocess.run(["ls", "-la", "jupyter*"])
    # print("----------------- whereis python")
    # subprocess.run(["whereis", "python"])
    print("----------------- whereis jupyter")
    subprocess.run(["whereis", "jupyter"])
    print("----------------- whereis jupyter-kernelspec")
    subprocess.run(["whereis", "jupyter-kernelspec", "list"])
    # print("----------------- pip install jupyter")
    # subprocess.run(["pip", "install", "jupyter"])

    try:
        notebook_name = event['notebook_name']
        notebook_file = create_temp_file()
        download_from_s3_bucket(DOWNLOAD_BUCKET, notebook_name, notebook_file)
    except Exception as exc:
        raise Exception("Failed to download notebook: %s from bucket: %s" % (notebook_name, DOWNLOAD_BUCKET)) from exc

    try:
        notebook_html_file = convert_to_html_file(notebook_file)
    except Exception as exc:
        print(exc)
        raise Exception("Failed to convert notebook: %s from bucket: %s" % (notebook_name, DOWNLOAD_BUCKET)) from exc

    try:
        notebook_html_name = notebook_name.split(".")[0] + ".html"
        upload_to_s3_bucket(notebook_html_file, UPLOAD_BUCKET, notebook_html_name)
    except Exception as exc:
        raise Exception("Failed to upload html at bucket: %s with key %s" % (UPLOAD_BUCKET, notebook_html_name)) from exc

    try:
        delete_temp_files(notebook_file, notebook_html_file)
    except:
        print("Warning: failed to delete temp files")
