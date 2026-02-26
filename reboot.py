import boto3

ec2 = boto3.client('ec2')

INSTANCE_ID = "i-0c3e91a4394ec8556"

def lambda_handler(event, context):
    print("Alarm triggered. Rebooting EC2 instance...")
    
    ec2.reboot_instances(
        InstanceIds=[INSTANCE_ID]
    )

    return "EC2 Instance Rebooted Sucessfully"
