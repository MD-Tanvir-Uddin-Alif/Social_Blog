from typing import Any
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .import models


class User_profile_Form(UserCreationForm):
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)
    phone_number = forms.CharField(max_length=12)
    profile_picture = forms.ImageField()

    class Meta:
        model = User
        fields = ['first_name','last_name','username','password1','password2','phone_number','email','profile_picture']


class User_Profile_Edit_Form(forms.ModelForm):
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)
    email = forms.EmailField()
    phone_number = forms.CharField(max_length=12)
    profile_picture = forms.ImageField(required=False)

    class Meta:
        model = models.User_profile
        fields = ['phone_number','profile_picture']

    def __init__(self, *args, **kwargs):
        user_instance = kwargs.pop('user_instance', None)
        super(User_Profile_Edit_Form, self).__init__(*args, **kwargs)

        if user_instance:
            self.user_instance = user_instance 
            self.fields['first_name'].initial = user_instance.first_name
            self.fields['last_name'].initial = user_instance.last_name
            self.fields['email'].initial = user_instance.email

    def save(self, commit=True):
        user_instance = self.user_instance
        user_instance.first_name = self.cleaned_data['first_name']
        user_instance.last_name = self.cleaned_data['last_name']
        user_instance.email = self.cleaned_data['email']

        if commit:
            user_instance.save()
            profile_instance = super(User_Profile_Edit_Form, self).save(commit=False)
            profile_instance.user = user_instance
            profile_instance.save()


        return user_instance 

