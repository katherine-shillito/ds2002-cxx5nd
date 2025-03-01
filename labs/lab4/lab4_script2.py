import boto3
import requests
import sys

def fetch_file(url, local_filename):
    response = requests.get(url)
    with open(local_filename, 'wb') as file:
        file.write(response.content)
    print(f"File downloaded as {local_filename}")

def upload_file(local_filename, bucket_name):
    s3 = boto3.client('s3', region_name='us-east-1')
    s3.upload_file(local_filename, bucket_name, local_filename)
    print(f"File uploaded to {bucket_name}")

def generate_url(bucket_name, object_name, time):
    s3 = boto3.client('s3', region_name='us-east-1')
    presigned_url = s3.generate_presigned_url(
        'get_object',
        Params={'Bucket': bucket_name, 'Key': object_name},
        ExpiresIn=time
    )
    return presigned_url

if __name__ == "__main__":
    url = sys.argv[1]
    local_filename = sys.argv[2]
    bucket_name = sys.argv[3]
    time = int(sys.argv[4])

    fetch_file(url, local_filename)
    upload_file(local_filename, bucket_name)
    presigned_url = generate_url(bucket_name, local_filename, time)
    print(f"Presigned URL: {presigned_url}")