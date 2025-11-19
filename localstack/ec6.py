import boto3

# Create a boto3 session
aws_management_console = boto3.session.Session()

# EC2 resource
aws_management_resource = aws_management_console.resource(
    service_name="ec2",
    region_name="us-east-1",  # Corrected region
    endpoint_url="http://localhost:4566",
    aws_access_key_id="test",
    aws_secret_access_key="test"
)

# EC2 client (not needed for stopping, but okay to keep)
aws_management_client = aws_management_console.client(
    service_name="ec2",
    region_name="us-east-1",
    endpoint_url="http://localhost:4566",
    aws_access_key_id="test",
    aws_secret_access_key="test"
)

# Iterate over all instances and stop them
for instance in aws_management_resource.instances.all():
    print(f"Stopping instance {instance.id}...")
    response = instance.start()
    print(f"Instance {instance.id} stop response: {response}")

for instance in aws_management_resource.instances.limit(count=2):
    print(f"Stopping instance {instance.id}...")
    response = instance.stop()
    print(f"Instance {instance.id} stop response: {response}")





