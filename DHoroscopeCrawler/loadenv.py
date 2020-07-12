###


####
import os
import boto3
from collections import defaultdict
import socket

from dotenv import load_dotenv

load_dotenv()


def get_info():
    AWS_ACCESS_KEY_ID = os.environ['AWS_ACCESSKEY']
    AWS_SECRET_ACCESS_KEY = os.environ['AWS_SECRETKEY']
    AWS_VPC = os.environ['AWS_VPC']
    ec2 = boto3.resource('ec2', region_name='us-west-2', aws_access_key_id=AWS_ACCESS_KEY_ID,
                         aws_secret_access_key=AWS_SECRET_ACCESS_KEY)
    vpc = ec2.Vpc(AWS_VPC)
    instance_iterator = vpc.instances.all()
    for i in instance_iterator:
        for tag in i.tags:
            print(tag)
            if tag['Key'] == 'Name':
                print(tag['Value'])


def getenvironment():
    AWS_ACCESS_KEY_ID = os.environ['AWS_ACCESSKEY']
    AWS_SECRET_ACCESS_KEY = os.environ['AWS_SECRETKEY']

    # Connect to EC2
    ec2 = boto3.resource('ec2', region_name='us-west-2', aws_access_key_id=AWS_ACCESS_KEY_ID,
                         aws_secret_access_key=AWS_SECRET_ACCESS_KEY)

    # Get information for all running instances
    running_instances = ec2.instances.filter(Filters=[{
        'Name': 'instance-state-name',
        'Values': ['running']}])

    ec2info = defaultdict()
    for instance in running_instances:
        for tag in instance.tags:
            if 'Name' in tag['Key']:
                name = tag['Value']
        # Add instance info to a dictionary
        ec2info[instance.id] = {
            'Name': name,
            'Type': instance.instance_type,
            'State': instance.state['Name'],
            'Private IP': instance.private_ip_address,
            'Public IP': instance.public_ip_address,
            'Launch Time': instance.launch_time
        }

    attributes = ['Name', 'Type', 'State', 'Private IP', 'Public IP', 'Launch Time']
    for instance_id, instance in ec2info.items():
        for key in attributes:
            # print("{0}: {1}".format(key, instance[key]))
            if key == 'Private IP':
                # print(instance[key])
                s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                s.connect(('8.8.8.8', 1))  # connect() for UDP doesn't send packets
                local_ip_address = s.getsockname()[0]
                print(local_ip_address)
                if local_ip_address == instance[key]:
                    # print("AWS")
                    return os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'DHoroscopeCrawler.settings.production')
                else:
                    # print("Local")
                    return os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'DHoroscopeCrawler.settings.development')
