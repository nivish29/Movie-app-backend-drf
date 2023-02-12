from django.contrib import admin
from django.urls import path
from userApp.api.views import userGetCreate,userGetUpdateDelete

urlpatterns = [
    path('',userGetCreate.as_view(),name='create-findUser'),
    path('<int:pk>',userGetUpdateDelete.as_view(),name='update-delete-findUser'),
    
]
