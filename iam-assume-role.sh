#!/bin/bash

# Task # 1 How to create and assume an IAM Role for a developer and attach appropriate policy
# Retrieve the ARN for the  user (i.e. developer) and set  it as a variable  name PRINCIPAL_ARN
PRINCIPAL_ARN=$(aws sts get-caller-identity --query Arn --output text)

# Use the sed command to replace PRINCIPAL_ARN in the assume-role-policy-template.json file
# and generate the assume-role-policy.json file
sed -e "s|PRINCIPAL_ARN|${PRINCIPAL_ARN}|g" assume-role-policy-template.json > assume-role-policy.json

# Create a  role and specify the assume role policy file
ROLE_ARN=$(aws iam create-role --role-name iam_assume_role \
     --assume-role-policy-document file://assume-role-policy.json \
     --output text --query Role.Arn)


# Attach  the AWS managed PowerUserAccess policy to the  role
aws iam attach-role-policy --role-name iam_assume_role \
     --policy-arn arn:aws:iam::aws:policy/PowerUserAccess


# Attach  the AWS managed PowerUserAccess  policy to the role
aws iam attach-role-policy --role-name iam_assume_role \
     --policy-arn arn:aws:iam::aws:policy/PowerUserAccess


# Validation  checks - Assume the role
aws sts assume-role --role-arn $ROLE_ARN \
     --role-session-name IAM_ROLE_DEV
