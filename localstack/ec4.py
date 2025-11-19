import boto3
from pprint import pprint 

# Create a boto3 session (profile not needed for LocalStack)
aws_management_console = boto3.session.Session()

# EC2 resource
aws_management_resource = aws_management_console.resource(
    service_name="ec2",
    region_name="us-east-1",
    endpoint_url="http://localhost:4566",  # LocalStack API URL
    aws_access_key_id="test",
    aws_secret_access_key="test"
)

# EC2 client
aws_management_client = aws_management_console.client(
    service_name="ec2",
    region_name="us-east-1",
    endpoint_url="http://localhost:4566",  # LocalStack API URL
    aws_access_key_id="test",
    aws_secret_access_key="test"
)


response = aws_management_client.describe_instances()["Reservations"]

for reservation in response:
    for instance in reservation.get("Instances", []):
        instance_id = instance.get("InstanceId")
        instance_type = instance.get("InstanceType")
        image_id = instance.get("ImageId")
        print(f"Instance ID: {instance_id}, Type: {instance_type}, Image: {image_id}")
