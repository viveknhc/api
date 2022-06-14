from django.shortcuts import render
from serializers import UserRegister
from rest_framework.views import APIview 
# Create your views here.
class register(APIview):

    def post(self,request,format=None):
        serializer = UserRegister(data=request.data) 