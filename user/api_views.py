import json

from django.http import JsonResponse
from rest_framework import viewsets

from user.models import User
from user.serializers import UserSerializer


class UserAPIView(viewsets.ModelViewSet):
    serializer_class = UserSerializer

    def userData(self, request):
        secret_code=request.query_params.get('secret_code')
        user=User.objects.filter(secret_code=secret_code)
        if user:
            serializer_data = UserSerializer(user, many=True)
            user_details = json.dumps(serializer_data.data)
            user_details = json.loads(user_details)

            data = {
                'user_detils': user_details
            }
        else:
            data = {
                'message': 'Record Not Found'
            }

        return JsonResponse(data)
