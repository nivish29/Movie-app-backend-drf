from rest_framework import generics
from userApp.models import findUser
from userApp.api.serializers import FindUserSerializer

class userGetCreate(generics.ListCreateAPIView):
    queryset=findUser.objects.all()
    serializer_class=FindUserSerializer

class userGetUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset=findUser.objects.all()
    serializer_class=FindUserSerializer