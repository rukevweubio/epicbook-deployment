import boto3

session = boto3.session.Session()

ec2 = session.resource(
    service_name="ec2",
    region_name="us-east-1",
    endpoint_url="http://localhost:4566",
    aws_access_key_id="test",
    aws_secret_access_key="test"
)

# Create a test instance
instances = ec2.create_instances(
    ImageId="ami-12345678",
    MinCount=1,
    MaxCount=1,
    InstanceType="t2.micro"
)

instance_id = instances[0].id
print(f"Created instance: {instance_id}")

# Now stop it
response = ec2.meta.client.stop_instances(InstanceIds=[instance_id])
print(f"Stopped instance: {response}")
