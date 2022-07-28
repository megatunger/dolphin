import requests
from django.http import JsonResponse
from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.decorators import api_view
from nanoid import generate
from dolphin import settings
from widget.models import ScalarToken


@api_view(['GET', 'POST'])
def account(request):
    scalarToken = request.query_params["scalar_token"]
    scalar = ScalarToken.objects.get(scalarToken=scalarToken)
    return JsonResponse({
        "user_id": scalar.userId
    }, status=status.HTTP_200_OK)

@api_view(['GET', 'POST'])
def register(request):
    url = f'{settings.env("SYNAPSE_SERVER")}/_matrix/federation/v1/openid/userinfo?access_token={request.data["access_token"]}' # Transform scalar token to user id
    result = requests.get(url)
    userId = result.json()['sub']
    sytToken = ''
    try:
        url = f'{settings.env("SYNAPSE_SERVER")}/_synapse/admin/v1/users/{userId}/login'
        result = requests.post(url, headers={"Authorization": f'Bearer {settings.env("ADMIN_TOKEN")}'}) # Save syt token to manipulate message
        sytToken = result.json()['access_token']
    except:
        sytToken = settings.env("ADMIN_TOKEN")
    scalar = ScalarToken.objects.create(userId=userId, scalarToken=generate(), sytToken=sytToken)
    return JsonResponse({
        "scalar_token": scalar.scalarToken
    }, status=status.HTTP_200_OK)

