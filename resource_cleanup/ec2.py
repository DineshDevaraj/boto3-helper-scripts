
import boto3

from pprint import pprint
from metaclass_definitions import Singleton

class EC2(metaclass=Singleton):

    c = None # client

    def __init__(self):

        self.init()

    @staticmethod
    def init():

        if EC2.c is None:
            EC2.c = boto3.client("ec2");

    @staticmethod
    def delete_instances():
        
        print("Delete EC2 Instances in progress")
        resp = EC2.c.describe_instances(Filters=[{
            'Name': 'instance-state-name',
            'Values': ['pending', 'running', 'shutting-down', 'stopping', 'stopped']
        }])
        # pprint(resp)
        instIdList = []
        for reservation in resp["Reservations"]:
            for ec2Inst in reservation["Instances"]:
                instIdList.append(ec2Inst["InstanceId"])
        # pprint(instIdList)
        if instIdList:
            EC2.c.terminate_instances(InstanceIds=instIdList)
            waiter = EC2.c.get_waiter('instance_terminated')
            waiter.wait(InstanceIds=instIdList)
        pass

    @staticmethod
    def delete_security_groups():
        
        print("Delete Security Groups in progress")
        resp = EC2.c.describe_security_groups()
        # pprint(resp)
        for secGroup in resp["SecurityGroups"]:
            EC2.c.delete_security_group(
                GroupId=secGroup["GroupId"]
            )
        pass
