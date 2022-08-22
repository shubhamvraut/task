import json

from django.http import JsonResponse
from rest_framework import viewsets
from rest_framework.authtoken.models import Token

from user.models import User
from user.serializers import UserSerializer

class LoginView(viewsets.ModelViewSet):

    def post(self,request):
        login_details = data = request.data
        try:
            user = User.objects.get(username=login_details['username'], password=login_details['password'])
            token, created = Token.objects.get_or_create(user=user)
            data = {
                'id': user.id,
                'username': user.username,
                'mobile_no': user.mobile_no,
                'secret_code': user.secret_code,
               'token': token.key,
            }
            return JsonResponse(data)
        except User.DoesNotExist:
                return JsonResponse({'message': "Username / password not matched"})


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
