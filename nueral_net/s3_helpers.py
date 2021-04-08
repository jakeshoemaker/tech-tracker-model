import boto3
from botocore.exceptions import ClientError
import logging

s3 = boto3.client('s3')
response = s3.list_buckets()

# Output the bucket names
print('Existing buckets:')
for bucket in response['Buckets']:
    print(f'  {bucket["Name"]}')

def upload_file(file_name, bucket, object_name=None):
    """Upload a file to an S3 bucket

    :param file_nam: File to upload
    :param bucket: Bucket to upload to
    :param object_name: S3 object name, in not specified then file_name is used
    :return: True if successful, else False
    """

    # If S3 object name not specified, use file_name
    if object_name is None:
        object_name = file_name

    # Upload the file
    s3_client = boto3.client('s3')
    try:
        res = s3_client.upload_file(file_name, bucket, object_name)
    except ClientError as e:
        logging.error(e)
        return False
    print("Upload Successful: \n Uploaded {0} to {1}", file_name, bucket)
    return True


def download_file(file_name, bucket, object_name=None):
    """Download a file from the specified S3 bucket

    :param file_nam: File to download
    :param bucket: Bucket to download from
    :param object_name: S3 object name, in not specified then file_name is used
    :return: file_obj if successful, else throw err
    """
    successful = False
    if object_name is None:
        object_name = file_name

    s3_client = boto3.client('s3')
    # try downloading the file
    try:
        with open(file_name, 'wb') as f:
            s3.download_fileobj(bucket, object_name, f)
            model = f
        successful = True
    except ClientError as e:
        logging.error(e)
    
    if successful:
        return model
    else:
        print("Error downloading file obj")
        return 0
       

