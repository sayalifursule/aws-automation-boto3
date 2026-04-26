import boto3

s3 = boto3.client('s3')

bucket_name = "sayali-automation-bucket-123"

response = s3.create_bucket(
    Bucket=bucket_name,
    CreateBucketConfiguration={
        'LocationConstraint': 'ap-south-1'
    }
)

print("S3 Bucket Created:", bucket_name)