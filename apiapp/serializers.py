from dataclasses import field
from tkinter.ttk import Style
from django.forms import CharField
from rest_framework import serializers
from django.contrib.auth import get_user_model

User=get_user_model

class UserRegister(serializers.ModelSerilizer):
    password2 = serializers,CharField(style={'input_type':'password'}.write_only=True)


    class meta:
        model = User
        field = ["username","password","emai","password2"]

    def save(self):
        reg = User(
            email=self.validate_data['email']
            username=self.validate_data['username']

        )
        password = self.validate_date['password']
        password2 = self.validate_date['password2']

        if password != password2:
            raise serializers.ValidationError({'password','password does not match'})
        reg.set_password(password)
        reg.save()
        return reg()
