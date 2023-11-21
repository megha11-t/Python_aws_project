#import the library that we installed
import boto3

s3=boto3.resource('s3')
#first s3 is a variable in which we have stored the direct access of sr from our aws
ec2=boto3.resource('ec2')

c=0
for bucket in s3.buckets.all():
    print(bucket)
    c=c+1
    
#to print the number of buckets
print(c)

#if we only want the name of all buckets then
#instead do print(bucket.name)

#suppose we want to download a file present in our s3 bucket
# s3.Bucket("bucket_name").download_file("filename_to download","nameofile_withwhichwe_want-tosave-in-our-system") 
#s3.Bucket becoz we want to access the buckets from s3 and if we want to upload any file then use upload_file()

"""
upload_to_bucket(s3,file_name,bucket_name,key_name):
    print("Uploading file to S3")
    data = open(file_name, 'rb')
    s3.Bucket(bucket_name).put_object(Key=key_name,Body=data)
    print("File uploaded to S3")
"""