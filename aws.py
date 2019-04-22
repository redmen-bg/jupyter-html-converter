import boto3, botocore

s3_client = boto3.client('s3')

download_from_s3_bucket = s3_client.download_file

upload_to_s3_bucket = s3_client.upload_file
