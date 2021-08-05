from django import forms
from django.db import models
from django.db.models import fields  
from. models import Company_Data,UserProfile, Login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User 

class Company_DataForm(forms.ModelForm):  
    class Meta:  
        model = Company_Data  
        fields = "__all__"  
 
class SignUpForm(UserCreationForm):
    username = forms.CharField(max_length=100)
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    email = forms.EmailField()
    password1 = forms.CharField(label="", widget=forms.TextInput(attrs={'type': 'hidden'}))
    password2 = forms.CharField(label="", widget=forms.TextInput(attrs={'type': 'hidden'}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

class UserProfileForm(forms.ModelForm):  
    class Meta:  
        model = UserProfile  
        fields = "__all__" 

class loginForm(forms.ModelForm):
    class Meta:
        model = Login
        fields = "__all__"