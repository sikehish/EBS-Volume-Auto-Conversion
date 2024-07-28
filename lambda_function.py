import boto3

def get_volume_id(vol_arn):
    return vol_arn.split(":")[-1].split("/")[-1]

def lambda_handler(event, context):
    # extract vol id from event
    vol_id = get_volume_id(event["resources"][0])
    
    ec2_client = boto3.client('ec2')
    
    volume_info = ec2_client.describe_volumes(VolumeIds=[vol_id])
    current_type = volume_info['Volumes'][0]['VolumeType']
    
    if current_type == 'gp2':
        # Modify the volume to gp3
        res = ec2_client.modify_volume(
            VolumeId=vol_id,
            VolumeType='gp3'
        )
        # print(event)
        print(res)
        return {
            'statusCode': 200,
            'body': f'Volume {vol_id} modified to gp3.'
        }
    else:
        return {
            'statusCode': 200,
            'body': f'Volume {vol_id} is already of type {current_type}, no modification needed.'
        }
