import boto3
import json
import sqs_conf
import traceback


def receive_job_from_sqs():
    try:
        sqs = boto3.client('sqs')
        response = sqs.receive_message(
            QueueUrl=sqs_conf['url'],
            MaxNumberOfMessages=1,
            VisibilityTimeout=0,
            WaitTimeSeconds=0
        )

        if 'Messages' in response:
            message = response['Messages']
            res = message[0]
            payload = {
                'body': json.loads(res['Body']),
                'receipt_handle': res['ReceiptHandle']
            }
            print(payload)
    except:
        print(traceback.print_exc())


def push_job_to_sqs(job):
    try:
        sqs = boto3.client('sqs')
        sqs.send_message(
            QueueUrl=sqs_conf['url'],
            DelaySeconds=5,
            MessageBody=json.dumps(job)
        )
    except:
        print(traceback.print_exc())


def delete_job_from_sqs(handle):
    try:
        sqs = boto3.client('sqs')
        sqs.delete_message(
            QueueUrl=sqs_conf['url'],
            ReceiptHandle=handle
        )
    except:
        print(traceback.print_exc())
