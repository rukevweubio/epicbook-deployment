import boto3

s3 = boto3.client(
    "s3",
    endpoint_url="http://localhost:4566",
    aws_access_key_id="test",
    aws_secret_access_key="test",
    region_name="us-east-1"
)

bucket_name = "my-local-bucket"

print(f"Creating bucket: {bucket_name}")
s3.create_bucket(Bucket=bucket_name)

print("Listing buckets:")
print(s3.list_buckets())
