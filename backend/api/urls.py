from api import views as api_views
from django.urls import path

urlpatterns = [

    # Authentication Endpoints

    path("user/token/", api_views.MyTokenObtainPairView.as_view()), # pass it sa view method
    # http://127.0.0.1:8000/api/v1/user/token/ - try to login with existing acount to get token
    # go to jwtio pass the token
    # token as membership card - check for user info
]