#!/bin/bash

local_file=$1
bucket_name=$2
expiration_time=$3

# upload file to s3 bucket
aws s3 cp "$local_file" "s3://$bucket_name/"

# presign URL to file with a 7 day expiration time
aws s3 presign --expires-in "$expiration_time" "s3://$bucket_name/$(basename "$local_file")" 

