from django.urls import path

from user.api_views import UserAPIView
from user.views import  UpdateUser, GenerateQrcode

urlpatterns = [

    path('create/<int:id>/', UpdateUser.as_view(), name='update-user'),
    path('update/<int:id>/',UpdateUser.as_view(),name='update-user'),
    path('generate-qrcode/<int:id>/',GenerateQrcode.as_view(),name='update-user'),
    path('get-data/',UserAPIView.as_view({'get':'userData'}))
]
