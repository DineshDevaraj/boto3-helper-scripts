
from elb import ELB
from ec2 import EC2
from vpc import VPC
from autoscaling import AutoScaling

def cleanup_elb():

    ELB.delete_load_balancers()
    ELB.delete_target_groups()

def cleanup_autoscaling():
    
    AutoScaling.delete_auto_scaling_groups()
    
def cleanup_ec2_instances():
    
    EC2.delete_instances()

def cleanup_vpc():

    VPC.delete_internet_gateways()
    VPC.delete_subnets()
    VPC.delete_vpc()

def cleanup_security_group():

    EC2.delete_security_groups()

def main():

    EC2.init()
    ELB.init()
    VPC.init()
    AutoScaling.init()

    cleanup_elb()
    cleanup_autoscaling()
    cleanup_ec2_instances()
    cleanup_vpc()
    cleanup_security_group() 

if __name__ == "__main__":

    main()
