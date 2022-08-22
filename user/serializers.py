from rest_framework import serializers

from user.models import User


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model=User
        fields = ['mobile_no', 'address', 'city', 'profile_pic','username','secret_code','qr_code']