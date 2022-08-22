from django import forms

from user.models import User


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('mobile_no', 'address', 'city', 'profile_pic','username','secret_code')

