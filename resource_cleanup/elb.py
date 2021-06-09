
import boto3

from pprint import pprint
from metaclass_definitions import Singleton

class ELB(metaclass=Singleton):

    c = None # client

    def __init__(self):

        self.init()

    @staticmethod
    def init():

        if ELB.c is None:
            ELB.c = boto3.client("elbv2")

    @staticmethod
    def delete_target_groups():
        
        print("Delete Target Groups in progress")
        resp = ELB.c.describe_target_groups()
        # pprint(resp)
        for targetGroup in resp["TargetGroups"]:
            ELB.c.delete_target_group(
                TargetGroupArn=targetGroup["TargetGroupArn"]
            )    
        pass

    @staticmethod
    def delete_load_balancers():

        print("Delete Load Balancers in progress")
        resp = ELB.c.describe_load_balancers()
        # pprint(resp)
        lbArnList = []
        for loadBalancer in resp["LoadBalancers"]:
            lbArnList.append(loadBalancer["LoadBalancerArn"])
            ELB.c.delete_load_balancer(
                LoadBalancerArn=loadBalancer["LoadBalancerArn"]
            )
        if lbArnList:
            waiter = ELB.c.get_waiter("load_balancers_deleted")
            waiter.wait(LoadBalancerArns=lbArnList)
        pass
