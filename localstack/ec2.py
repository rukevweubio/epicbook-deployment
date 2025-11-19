import boto3

# Create Session (profile not needed for LocalStack)
aws_manage = boto3.session.Session()

# EC2 resource
aws_re_manage = aws_manage.resource(
    service_name="ec2",
    region_name="us-east-1",
    endpoint_url="http://localhost:4566",
    aws_access_key_id="test",
    aws_secret_access_key="test"
)

# EC2 client
aws_client = aws_manage.client(
    service_name="ec2",
    region_name="us-east-1",
    endpoint_url="http://localhost:4566",
    aws_access_key_id="test",
    aws_secret_access_key="test"
)

print(dir(aws_re_manage.instances))

# Loop through all instances
for each_in in aws_re_manage.instances.all():  # <-- plural 'instances'
    print(each_in.id, each_in.state)
