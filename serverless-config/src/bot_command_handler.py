from instance_manager import InstanceManager


class BotCommandHandler:

    instanceManager = InstanceManager()

    def handle(self, message):
        try:
            if "run" in message:
                return self.__start()

            if "stop" in message:
                return self.__stop()

            if "state" in message:
                return self.__get_state()
        except Exception as e:
            print(e)
            return e

        print("Unknown command called")
        return "Please, send one of the commands:\n" \
               "/run - to start instance\n" \
               "/stop - to stop instance\n" \
               "/state - to see instance state"

    def __start(self):
        print("'run' command called")
        self.instanceManager.start_instances()
        return 'Instance started'

    def __stop(self):
        print("'stop' command called")
        self.instanceManager.stop_instances()
        return 'Instance stopped'

    def __get_state(self):
        print("'state' command called")
        return self.instanceManager.get_instance_states()
