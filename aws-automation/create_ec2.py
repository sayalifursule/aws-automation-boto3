import boto3

ec2 = boto3.resource('ec2')

instance = ec2.create_instances(
    ImageId='ami-0f58b397bc5c1f2e8',  # Amazon Linux (ap-south-1)
    MinCount=1,
    MaxCount=1,
    InstanceType='t2.micro',
    KeyName='your-keypair-name'
)

print("EC2 Instance Created:", instance[0].id)