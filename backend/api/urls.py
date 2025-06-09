from api import views as api_views
from django.urls import path

from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [

    # Authentication Endpoints

    path("user/token/", api_views.MyTokenObtainPairView.as_view()), # pass it sa view method
    # http://127.0.0.1:8000/api/v1/user/token/ - try to login with existing acount to get token
    # go to jwtio pass the token
    # token as membership card - check for user info
    path("user/token/refresh/", TokenRefreshView.as_view()), #  get refresh token from http://127.0.0.1:8000/api/v1/user/token/  and pass it  http://127.0.0.1:8000/api/v1/user/token/refresh/
    path("user/register/", api_views.RegisterView.as_view()), # http://127.0.0.1:8000/api/v1/user/register/
    path("user/password-reset/<email>/", api_views.PasswordResetEmailVerifyAPIView.as_view()),
    path("user/password-change/", api_views.PasswordChangeAPIView.as_view()),
    
   

]