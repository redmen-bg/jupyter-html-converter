import boto3

s3_client = boto3.client('s3')

# def download_from_s3_bucket(bucket_name, key_name, file_path):
#     s3_client.download_file(bucket_name, key_name, file_path)

# def upload_to_s3_bucket(file_path, bucket_name, key_name):
#     s3_client.upload_file(file_path, bucket_name, key_name)

download_from_s3_bucket = s3_client.download_file

upload_to_s3_bucket = s3_client.upload_file