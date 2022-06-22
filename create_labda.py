import queue
from zipfile import ZipFile
import boto3
import os

AWS_REGION = 'us-east-1'
AWS_PROFILE = 'localstack'
ENDPOINT_URL = 'http://localhost.localstack.cloud:4566/'

boto3.setup_default_session(profile_name=AWS_PROFILE)

with open('function.zip', 'rb') as f:
    function=f.read()
    code = dict(ZipFile=function)

client = boto3.client('lambda',  endpoint_url=ENDPOINT_URL)
client.create_function(FunctionName='coleta-dados',  Runtime='python3.8', Role="arn:aws:iam::000000000000:role/lambda-role", Handler="lambda_handler", Code=code)

#awslocal sqs create-queue --queue-name sqs_requisicoes --endpoint-url=http://localhost:4566/