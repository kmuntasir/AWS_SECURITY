import boto3

resource = boto3.resource("s3")

iterator = resource.buckets.all()

print("Listing Amazon S3 Buckets:")

for bucket in iterator:
    print(f"-- {bucket.name}")