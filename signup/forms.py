from django import forms 
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
  
class signup_detail(UserCreationForm):
    first_name=forms.CharField(max_length=25)
    last_name=forms.CharField(max_length=25)
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model=User
        fields=['username','email','first_name','last_name','password1','password2']

class LoginForm(forms.Form):
    username=forms.CharField(max_length=25)
    password=forms.CharField(widget=forms.PasswordInput)
