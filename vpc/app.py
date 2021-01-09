#!/usr/bin/env python3

from aws_cdk import core

from ec2.ec2_stack import Ec2Stack


app = core.App()
Ec2Stack(app, "ec2", env={'region': 'ap-northeast-2'})

app.synth()
