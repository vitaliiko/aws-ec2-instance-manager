from instance_manager import InstanceManager


def start_instances(event, context):
    InstanceManager().start_instances()


def stop_instances(event, context):
    InstanceManager().stop_instances()
