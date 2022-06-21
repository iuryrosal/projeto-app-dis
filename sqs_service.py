import queue
import boto3
import os

AWS_REGION = 'us-east-1'
AWS_PROFILE = 'localstack'
ENDPOINT_URL = os.environ.get('LOCALSTACK_ENDPOINT_URL')

boto3.setup_default_session(profile_name=AWS_PROFILE)

class SQSService:
    def __init__(self) -> None:
        self.client = boto3.client('sqs',  endpoint_url=ENDPOINT_URL)

    def send_message(self, sqs_url, message):
        response = self.client.send_message(QueueUrl = sqs_url, 
                                            MessageBody = message)
        return response

#awslocal sqs create-queue --queue-name sqs_requisicoes --endpoint-url=http://localhost:4566/