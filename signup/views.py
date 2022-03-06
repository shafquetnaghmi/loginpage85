from django.shortcuts import render
from .forms  import signup_detail,LoginForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponseRedirect
from django.urls import reverse 
from django.shortcuts import redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages


def home(request):
    return render(request,'signup/home.html')

def registerpage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form=signup_detail()
        if request.method=='POST':
          form=signup_detail(request.POST)
          if form.is_valid():
           form.save()
           
           username=form.cleaned_data.get('username')
           email=form.cleaned_data.get('email')
           raw_password=form.cleaned_data.get('password1')
           #user=authenticate(username=username,passowrd=raw_password)
           return redirect('signup:login')
        else:
            form=signup_detail()
    return render(request,'signup/registration.html',{'form':form})

def loginpage(request):
    #form=AuthenticationForm(request)
    if request.method=='POST':
      username = request.POST.get('username')
      password = request.POST.get('password')
      user = authenticate(request, username=username, password=password)
      
      if user is not None:
         login(request, user)
         messages.success(request, 'welcome')
         return HttpResponseRedirect(reverse("signup:home"))
      else:
         messages.info(request, 'account does not exit plz sign in')
    
    return render(request,'signup/loginpage.html',)

def logoutpage(request):
    logout(request)
    return HttpResponseRedirect(reverse("signup:home"))
