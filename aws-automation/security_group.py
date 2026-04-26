import boto3

ec2 = boto3.client('ec2')

response = ec2.create_security_group(
    GroupName='my-security-group',
    Description='Allow SSH'
)

sg_id = response['GroupId']

ec2.authorize_security_group_ingress(
    GroupId=sg_id,
    IpPermissions=[
        {
            'IpProtocol': 'tcp',
            'FromPort': 22,
            'ToPort': 22,
            'IpRanges': [{'CidrIp': '0.0.0.0/0'}]
        }
    ]
)

print("Security Group Created:", sg_id)