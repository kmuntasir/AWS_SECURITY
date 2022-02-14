
import  boto3
import  json

# The following program allows full access to view and edit the account password policy.
# You must configure permissions to allow an IAM entity (user or role) to view or edit their account password policy.

# Create IAM client
client = boto3.client('iam')

policy_json = {

    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "FullAccessPasswordPolicy",
            "Effect": "Allow",
            "Action": [
                "iam:GetAccountPasswordPolicy",
                "iam:DeleteAccountPasswordPolicy",
                "iam:UpdateAccountPasswordPolicy"
            ],
            "Resource": "*"
        }
    ]
}

response = client.create_policy(
    PolicyName='ClientFullAccessPasswordPolicy',
    PolicyDocument=json.dumps(policy_json)
) 

print(response['Policy'])


