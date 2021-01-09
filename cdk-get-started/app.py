#!/usr/bin/env python3

from aws_cdk import core

from cdk_serverless_get_started.cdk_serverless_get_started_stack import CdkServerlessGetStartedStack

app = core.App()
CdkServerlessGetStartedStack(app, "cdk-serverless-get-started", env={'region': 'ap-northeast-2'})

app.synth()

