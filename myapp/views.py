from django.shortcuts import render
from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
# from django.contrib.auth.decorators import login_required
from myapp import *

# Create your views here.
def home_view(request):
    # Your logic for the home view
    return render(request, 'home.html') 

def login_view(request):
    if request.method=='POST':
        username=request.POST.get('username')
        pass1=request.POST.get('pass')
        user=authenticate(request,username=username,password=pass1)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            return HttpResponse("Username or password is incorrec!!!")
    return render(request, 'login.html')




def register_view(request):
    if request.method=='POST':
        uname=request.POST.get('username')
        email=request.POST.get('email')
        pass1=request.POST.get('password1')
        pass2=request.POST.get('password2')
        
        if pass1!=pass2:
            return HttpResponse("Your password and confirm password are not same !!")
        else:
            my_user=User.objects.create_user(uname,email,pass1)
            my_user.save()
            return  redirect('login')
      
        
        
    return render(request, 'register.html') 



def logout_view(request):
    logout(request)
    return redirect('home') 