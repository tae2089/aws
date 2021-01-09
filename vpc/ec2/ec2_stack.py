from aws_cdk import core
from aws_cdk import aws_ec2 as ec2
from aws_cdk import aws_iam

class Ec2Stack(core.Stack):

    def __init__(self, scope: core.Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # The code that defines your stack goes here
        # VPC 만들기
        vpc = ec2.Vpc(self, "test",cidr="10.200.0.0/24", 
        nat_gateways=0, 
        subnet_configuration=[ec2.SubnetConfiguration(name="public", subnet_type=ec2.SubnetType.PUBLIC)])
        #test
        
