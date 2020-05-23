import boto3
import os

region = os.environ['AWS_REGION']
instances = os.environ['INSTANCE_IDS']
ec2 = boto3.client('ec2', region_name=region)


def start_instances(event, context):
    ec2.start_instances(InstanceIds=instances.split(','))
    print('started instances: ' + str(instances))


def stop_instances(event, context):
    ec2.stop_instances(InstanceIds=instances.split(','))
    print('stopped instances: ' + str(instances))
