import json
import pytest

from aws_cdk import core
from cdk-serverless-get-started.cdk_serverless_get_started_stack import CdkServerlessGetStartedStack


def get_template():
    app = core.App()
    CdkServerlessGetStartedStack(app, "cdk-serverless-get-started")
    return json.dumps(app.synth().get_stack("cdk-serverless-get-started").template)


def test_sqs_queue_created():
    assert("AWS::SQS::Queue" in get_template())


def test_sns_topic_created():
    assert("AWS::SNS::Topic" in get_template())
