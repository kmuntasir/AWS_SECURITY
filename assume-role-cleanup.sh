#!/bin/bash

# This script will delete the assumed IAM role
echo  "Please enter the assumed role name to delete : "
read    rolename

# First detach the policy "PowerUserAccess" attached with the role
aws iam detach-role-policy --role-name $rolename \
--policy-arn arn:aws:iam::aws:policy/PowerUserAccess 

# Delete the IAM role 
aws iam delete-role --role-name  $rolename

# unset local variables
unset ROLE_ARN
unset PRICIPAL_ARN

if  [rolename = $rolename]
then
	echo  "The assumed IAM_ROLE  $rolename has been deleted."
fi
