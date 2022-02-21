import boto3
s3  = boto3.client('s3')
bucket_name=str(input('please input bucket name to find the policy attached: '))
s3_policy = s3.get_bucket_policy(Bucket=bucket_name)
print(s3_policy['Policy'])
   
# Delete a bucket's policy
response=str(input('Do you want to delete the bucket policy? y/n:  '))
while (response != 'y' and response != 'n'):
    response = input("error: wrong input. Please put y or n only ")
if (response == 'y'):
  s3 = boto3.client('s3')
  s3.delete_bucket_policy(Bucket=bucket_name)
   
  
 
