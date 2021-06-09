
import boto3

from metaclass_definitions import Singleton
from pprint import pprint
from ec2 import EC2

class VPC(metaclass=Singleton):

    def __init__(self):

        self.init()

    @staticmethod
    def init():

        EC2.init()

    @staticmethod
    def __detach_internet_gateways(ingId, attList):
        for vpc in attList: 
            EC2.c.detach_internet_gateway(
                InternetGatewayId=ingId,
                VpcId=vpc["VpcId"]
            )
        pass

    @staticmethod
    def delete_internet_gateways():

        print("Delete Internet Gateways in progress")
        resp = EC2.c.describe_internet_gateways()
        # pprint(resp)
        for ingDict in resp["InternetGateways"]:
            ingId = ingDict["InternetGatewayId"]
            VPC.__detach_internet_gateways(ingId, ingDict["Attachments"])
            EC2.c.delete_internet_gateway(
                InternetGatewayId=ingId
            )
        pass

    @staticmethod
    def delete_subnets():
        
        print("Delete Subnets in progress")
        resp = EC2.c.describe_subnets()
        # pprint(resp)
        for subnet in resp["Subnets"]:
            EC2.c.delete_subnet(
                SubnetId=subnet["SubnetId"]
            )
        pass

    @staticmethod
    def delete_vpc():

        print("Delete Vpcs in progress")
        resp = EC2.c.describe_vpcs()
        # pprint(resp)
        for vpc in resp["Vpcs"]:
            EC2.c.delete_vpc(VpcId=vpc["VpcId"])
        pass
