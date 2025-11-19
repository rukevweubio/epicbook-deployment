import boto3

# Create boto3 session
aws_management_console = boto3.session.Session()

# EC2 client
aws_management_client = aws_management_console.client(
    service_name="ec2",
    region_name="us-east-1",
    endpoint_url="http://localhost:4566",
    aws_access_key_id="test",
    aws_secret_access_key="test"
)

# Describe volumes
response = aws_management_client.describe_volumes()

for volume in response["Volumes"]:
    print(f"Volume ID: {volume['VolumeId']}, State: {volume['State']}, Size: {volume['Size']} GB")
