#Name of the file: s3blist.py
#Author name: Shi Ling Chan
#Code purpose: List all S3 buckets and pipe to a file when required
#Date written: 13/02/2023
#Revision: 1

import boto3
#Instantiate the connection
answer=input('Please confirm the AWS default region is correct Answer:Yes/No')

s3 = boto3.client('s3')
#retrieve buckets
response = s3.list_buckets()['Buckets']
#Create a file to write bucket Name
file1 = open("lists3.txt", "w")
file1.close()
#loop through all buckets and display buckets
for bucket in response:
    if answer == 'No':
        exit()
    elif answer == 'Yes':
        #Open the text file 
        file2 = open("lists3.txt", "a")
        #For each bucket, print the name of the bucket to the file
        file2.write(bucket['Name'] + '\n')
        file2.close()
        #For each bucket, print the name and creation date onto the console
        print('Bucket name: {}, Created on: {}'.format(bucket['Name'], bucket['CreationDate']))

