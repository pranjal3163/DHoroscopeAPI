###


####
import os
import boto3

from dotenv import load_dotenv

load_dotenv()


def getenvironment():
    AWS_ACCESS_KEY_ID = os.environ['AWS_ACCESSKEY']
    AWS_SECRET_ACCESS_KEY = os.environ['AWS_SECRETKEY']
    AWS_VPC = os.environ['AWS_VPC']
    ec2 = boto3.resource('ec2', region_name='us-west-2', aws_access_key_id=AWS_ACCESS_KEY_ID,
                         aws_secret_access_key=AWS_SECRET_ACCESS_KEY)
    vpc = ec2.Vpc(AWS_VPC)
    instance_iterator = vpc.instances.all()
    for i in instance_iterator:
        for tag in i.tags:
            if tag['Key'] == 'Name':
                #print(tag['Value'])
                if tag['Value'] == 'DHoroscopeAPI':
                    return os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'DHoroscopeCrawler.settings.development')
                else:
                    return os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'DHoroscopeCrawler.settings.development')

