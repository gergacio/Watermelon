from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from userauths.models import Profile, User

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    # call it when we want to create token for particular user
    @classmethod # doesn't belongs to instance
    def get_token(cls, user):
        token = super().get_token(user) # call parent class

        # grab all from the user 
        # customize token - add extra info
        token['full_name'] = user.full_name
        token['email'] = user.email
        token['username'] = user.username
      
        return token

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User # include model and fields we want to serialize
        fields = '__all__'

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = "__all__"