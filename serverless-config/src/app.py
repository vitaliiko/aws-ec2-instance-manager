from instance_manager import InstanceManager

if __name__ == '__main__':
    response = InstanceManager().get_instance_states()
    print(response.encode("utf8"))
