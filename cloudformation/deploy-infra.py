from __future__ import division, print_function, unicode_literals
import os
from datetime import datetime
import logging
import json
import sys

import boto3
import botocore

# Global variables
cf = boto3.client('cloudformation', region_name=os.getenv("AWS_DEFAULT_REGION", 'us-east-2'))  # pylint: disable=C0103
log = logging.getLogger('deploy.cf.create_or_update')  # pylint: disable=C0103

def get_cfs_in_folder():

    templates = os.listdir("./")
    yaml_files = list(filter(lambda file_name: "yaml" in file_name, templates))
    yaml_files.sort()

    return yaml_files

def cf_stack_provision(stack_name, template, parameters):
    'Update or create stack'

    template_data = _parse_template(template)

    params = {
        'StackName': stack_name,
        'TemplateBody': template_data,
        'Parameters': parameters,
    }

    try:
        print('Creating {}'.format(stack_name))
        stack_result = cf.create_stack(**params)
        waiter = cf.get_waiter('stack_create_complete')
        print("...waiting for stack to be ready...")
        waiter.wait(StackName=stack_name)
    except botocore.exceptions.ClientError as ex:
        error_message = ex.response['Error']['Message']
        if error_message == 'No updates are to be performed.':
            print("No changes")
        else:
            raise

def _parse_template(template):
    with open(template) as template_fileobj:
        template_data = template_fileobj.read()
    cf.validate_template(TemplateBody=template_data)
    return template_data


def _parse_parameters(parameters):
    with open(parameters) as parameter_fileobj:
        parameter_data = json.load(parameter_fileobj)
    return parameter_data


def _stack_exists(stack_name):
    stacks = cf.list_stacks()['StackSummaries']
    for stack in stacks:
        if stack['StackStatus'] == 'DELETE_COMPLETE':
            continue
        if stack_name == stack['StackName']:
            return True
    return False


def json_serial(obj):
    """JSON serializer for objects not serializable by default json code"""
    if isinstance(obj, datetime):
        serial = obj.isoformat()
        return serial
    raise TypeError("Type not serializable")

def get_cf_outputs(stackname):
    response = cf.describe_stacks(StackName=stackname)
    outputs = response["Stacks"][0]["Outputs"]

    return outputs

def main():
    yaml_files = get_cfs_in_folder()
    
    # The VPC is out of loop because the VPC ID will be used in almost all stacks
    vpc_stack = yaml_files[0]
    stack_name = 'batalha-de-dados-vpc'
    params = [
            {'ParameterKey': 'EnvironmentName',
            'ParameterValue': 'batalha-de-dados-vpc'
            }
        ]

    cf_stack_provision(stack_name, vpc_stack, params)
    vpc_outputs = get_cf_outputs(stack_name)

    PUBLIC_SUBNET = ""
    VPC_ID = ""

    for output in vpc_outputs:
        if 'PublicSubnet1' in output['OutputKey']:
            PUBLIC_SUBNET = output['OutputValue']
        if 'VPC' in output['OutputKey']:
            VPC_ID = output['OutputValue']


    print(f"This IDS will be used in almost all CFS: {PUBLIC_SUBNET, VPC_ID}")
    

if __name__ == '__main__':
    main()
    