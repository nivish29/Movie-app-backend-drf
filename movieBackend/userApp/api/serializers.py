from rest_framework import serializers  
from userApp.models import findUser

class FindUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = findUser
        fields='__all__'
