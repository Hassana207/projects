
from django import forms
from django.contrib.auth.models import  User 
from django.contrib.auth.forms import UserCreationForm

# Create your models here.

class UserRegistration(UserCreationForm):
    class Meta :
        model = User 
        fields = ['username','password1','password2']
    


