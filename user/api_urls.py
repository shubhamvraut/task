from django.urls import path

from user.api_views import UserAPIView, LoginView

urlpatterns = [

    path('get-data/',UserAPIView.as_view({'get':'userData'})),
    path('login/',LoginView.as_view({'get':'post'}))

]