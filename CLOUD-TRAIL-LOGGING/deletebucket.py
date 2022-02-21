import io
import boto3

s3  = boto3.resource('s3')
bucket_name=str(input('please input bucket name to be deleted: '))
s3_bucket = s3.Bucket(bucket_name)

def cleanup_s3_bucket():
    # Deleting objects
    for s3_object in s3_bucket.objects.all():
        s3_object.delete()
 
objs = list(s3_bucket.objects.filter(Prefix='AWSLogs/'))
if(len(objs)>0):
    print("key exists!!")
    cleanup_s3_bucket()
    print("S3 Bucket cleaned up")
else:
    s3_bucket.delete()
    print("S3 Bucket deleted") 



