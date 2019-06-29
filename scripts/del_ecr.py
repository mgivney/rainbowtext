import os
import boto3

client = boto3.client('ecr')

ID = os.getenv('AWS_ACCOUNT_ID', 'your_AWS_id')
REGION = os.getenv('AWS_REGION', 'your_aws_region')

# Get the name of the current directory
PROJECT = os.path.basename(os.path.realpath("."))

# use if repository exist
SERVER_REPOSITORY_URI = f'{ID}.dkr.ecr.{REGION}.amazonaws.com/{PROJECT}_server'
NGINX_REPOSITORY_URI = f'{ID}.dkr.ecr.{REGION}.amazonaws.com/{PROJECT}_nginx'



for key, value in ECR_REPO_OBJ.items():
    response = client.delete_repository(
        registryId=AWS_ACCOUNT_ID,
        repositoryName=key,
        force=True
    )

    print(response)
