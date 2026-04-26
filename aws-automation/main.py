import boto3
import json
from botocore.exceptions import ClientError

REGION = "ap-south-1"
BUCKET_NAME = "sayali-aws-automation-202-001"   # 🔁 change if already taken
KEY_NAME = "my-keypair"

# ---------- S3 SETUP ----------
s3 = boto3.client("s3", region_name=REGION)

# 1. Create bucket (or reuse)
try:
    s3.create_bucket(
        Bucket=BUCKET_NAME,
        CreateBucketConfiguration={"LocationConstraint": REGION},
    )
    print("S3 bucket created")

except ClientError as e:
    if e.response["Error"]["Code"] == "BucketAlreadyOwnedByYou":
        print("Bucket already exists, using existing bucket")
    else:
        raise

# 2. Disable block public access
s3.put_public_access_block(
    Bucket=BUCKET_NAME,
    PublicAccessBlockConfiguration={
        "BlockPublicAcls": False,
        "IgnorePublicAcls": False,
        "BlockPublicPolicy": False,
        "RestrictPublicBuckets": False,
    },
)

# 3. Upload HTML file with correct content type
s3.upload_file(
    "index.html",
    BUCKET_NAME,
    "index.html",
    ExtraArgs={"ContentType": "text/html"},
)
print("File uploaded with correct content-type")

# 4. Enable static website hosting
s3.put_bucket_website(
    Bucket=BUCKET_NAME,
    WebsiteConfiguration={"IndexDocument": {"Suffix": "index.html"}},
)

# 5. Add public read policy
policy = {
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "PublicReadAccess",
            "Effect": "Allow",
            "Principal": "*",
            "Action": ["s3:GetObject"],
            "Resource": [f"arn:aws:s3:::{BUCKET_NAME}/*"],
        }
    ],
}

s3.put_bucket_policy(Bucket=BUCKET_NAME, Policy=json.dumps(policy))
print("Bucket policy applied")

# ---------- EC2 SETUP ----------
ec2_client = boto3.client("ec2", region_name=REGION)
ec2 = boto3.resource("ec2", region_name=REGION)

# 6. Create key pair if not exists
try:
    response = ec2_client.create_key_pair(KeyName=KEY_NAME)
    with open(f"{KEY_NAME}.pem", "w") as f:
        f.write(response["KeyMaterial"])
    print("Key pair created and saved")

except ClientError as e:
    if "InvalidKeyPair.Duplicate" in str(e):
        print("Key pair already exists")
    else:
        raise

# 7. Launch EC2 instance
instances = ec2.create_instances(
    ImageId="ami-0e742cca61fb65051",   # Amazon Linux (Mumbai)
    MinCount=1,
    MaxCount=1,
    InstanceType="t3.micro",
    KeyName=KEY_NAME,
)

instance = instances[0]
print("EC2 instance created:", instance.id)

# ---------- FINAL OUTPUT ----------
print("\n🌐 S3 Website URL:")
print(f"http://{BUCKET_NAME}.s3-website-{REGION}.amazonaws.com")