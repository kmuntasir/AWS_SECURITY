import boto3
import os

#Create an s3 bucket 
s3 = boto3.resource('s3')
bucket = s3.create_bucket(Bucket='mytestbuck2050',CreateBucketConfiguration={'LocationConstraint': 'ap-southeast-2'})
print (bucket)

# Replace the values in the cloudtrail-s3policy-template.json file with the values -bucketname & Acct ID from S3 deployment
var1 = 'sed -e "s/BUCKET_NAME/mytestbuck2050$RANDOM_STRING/g" -e "s|IAM_ADMIN|${IAM_ADMIN}|g" cloudtrail-s3policy-template.json > cloudtrail-s3policy.json'
os.system(var1)

# Add the s3 bucket policy to s3 bucket, you may need to replace AWS_ACCOUNT_ID with Account_ID 
var2 = 'aws s3api put-bucket-policy --bucket mytestbuck2050$RANDOM_STRING --policy file://cloudtrail-s3policy.json'
os.system(var2)

#Enable CloudTrail for all AWS Regions and configure the S3 bucket to send logs
var3 = 'aws cloudtrail create-trail --name AccountLoggingTrail --s3-bucket-name mytestbuck2050 --is-multi-region-trail'
os.system(var3)

# Create CloudTrail Trail in CloudTrail to start logging
var4 = 'aws cloudtrail start-logging --name AccountLoggingTrail' 
os.system(var4) 

# Describe the trail
var5 = 'aws cloudtrail describe-trails --trail-name-list AccountLoggingTrail'
os.system(var5)  

# Get the Trail status
var6 = 'aws cloudtrail get-trail-status --name AccountLoggingTrail'
os.system(var6) 

