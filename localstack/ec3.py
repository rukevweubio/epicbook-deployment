import boto3

# Connect to LocalStack
aws_manage = boto3.session.Session()

ec2_client = aws_manage.client(
    service_name="ec2",
    region_name="us-east-1",
    endpoint_url="http://localhost:4566",
    aws_access_key_id="test",
    aws_secret_access_key="test"
)

ec2_resource = aws_manage.resource(
    service_name="ec2",
    region_name="us-east-1",
    endpoint_url="http://localhost:4566",
    aws_access_key_id="test",
    aws_secret_access_key="test"
)

# Simulate creating 10 EC2 instances
print("Creating 10 EC2 instances in LocalStack...")

instances = ec2_client.run_instances(
    ImageId="ami-12345678",  # Dummy AMI for LocalStack
    MinCount=10,
    MaxCount=10,
    InstanceType="t2.micro"
)

# Print instance IDs
instance_ids = [inst["InstanceId"] for inst in instances["Instances"]]
print("Created instances:", instance_ids)

# Verify using resource
print("\nListing all instances via resource:")
for instance in ec2_resource.instances.all():
    print(f"ID: {instance.id}, State: {instance.state}")
