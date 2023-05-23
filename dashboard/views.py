from django.shortcuts import render
import boto3
from botocore.exceptions import NoCredentialsError


def dashboard_view(request):
    # Initialize Boto3 client for QuickSight
    client = boto3.client('quicksight', region_name='ap-southeast-2')

    # Retrieve the dashboard embed URL and pass it to the template
    try:
        response = client.get_dashboard_embed_url(
            AwsAccountId='233425133219',
            DashboardId='417175f2-cfb7-4feb-a21c-b9ae0723f6f3',
            IdentityType='IAM'
        )
        embed_url = response['EmbedUrl']
    except NoCredentialsError:
        # Handle error when AWS credentials are missing
        embed_url = None

    return render(request, 'dashboard.html', {'embed_url': embed_url})

