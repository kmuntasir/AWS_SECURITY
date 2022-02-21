Enabling CloudTrail Logging for Your AWS Account

here is the scenario - you have an AWS account and want to retain an audit log of all activites for all Regions 
in your account. 

Solution - Configure an S3 bucket with a bucket policy allowing CloudTrail to write events. 
Enable CloudTrail for all Regions in your account and configure CloudTrail to log 
all audit events to the S3 bucket.



