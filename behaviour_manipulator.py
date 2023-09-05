
import random
import time
import random, string
class BehaviourManipulator:

    def fake_human_behaviour(is_long_wait):
        wait_time = random.randint(2, 5)
        if(is_long_wait):
            wait_time = random.randint(5, 10)
        time.sleep(wait_time)

    def generate_fake_device_id():
        return BehaviourManipulator.generate_random_string(8)+"-"+BehaviourManipulator.generate_random_string(4)+"-"+BehaviourManipulator.generate_random_string(4)+"-"+BehaviourManipulator.generate_random_string(4)+"-"+BehaviourManipulator.generate_random_string(12)


    def generate_random_string(count):
        return ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(count))

