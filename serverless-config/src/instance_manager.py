import boto3
import os

region = os.environ['AWS_REGION']
instances = os.environ['INSTANCE_IDS']
ec2 = boto3.client('ec2', region_name=region)


class InstanceManager:

    instance_ids = instances.split(',')

    def start_instances(self):
        ec2.start_instances(InstanceIds=self.instance_ids)
        print('started instances: ' + str(instances))

    def stop_instances(self):
        ec2.stop_instances(InstanceIds=self.instance_ids)
        print('stopped instances: ' + str(instances))

    def reboot_instances(self):
        ec2.reboot_instances(InstanceIds=self.instance_ids)
        print('rebooted instances: ' + str(instances))

    def get_instance_states(self):
        response = ec2.describe_instances(InstanceIds=self.instance_ids)
        instance_descriptions = response['Reservations'][0]['Instances']

        result = []
        for instance in instance_descriptions:
            result.append({'Name': instance['KeyName'], 'State': instance['State']})
        return str(result)
