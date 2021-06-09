
import boto3

from pprint import pprint
from metaclass_definitions import Singleton

class AutoScaling(metaclass=Singleton):

    c = None # client

    def __init__(self):

        self.init()

    @staticmethod
    def init():

        if AutoScaling.c is None:
            AutoScaling.c = boto3.client("autoscaling");
        
    @staticmethod
    def delete_auto_scaling_groups():

        print("Delete Auto Scaling Groups in progress")
        resp = AutoScaling.c.describe_auto_scaling_groups()
        # pprint(resp)
        for asGroup in resp["AutoScalingGroups"]:
            AutoScaling.c.delete_auto_scaling_group(
                AutoScalingGroupName=asGroup["AutoScalingGroupName"]
            )
        pass
