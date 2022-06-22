from django.urls import path
from .views import RegistrationAPIView, LoginAPIView, UserRetrieveUpdateAPIView


app_name = 'app'


urlpatterns = [
    path('user/', UserRetrieveUpdateAPIView.as_view()),
    path('users/', RegistrationAPIView.as_view()),
    path('users/<int:pk>', RegistrationAPIView.as_view()),
    path('users/login/', LoginAPIView.as_view()),
]
