from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.
def index(request):
    if(request.user.is_anonymous):
        return redirect("/user/login")
    return render(request,'dashboard.html')

def loginUser(request):
    print(request.method)
    if request.method=="POST":
        print(request.POST.get('username'))
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username,password)
        user = authenticate(request,username=username,password=password)
        print(user)
        if user is not None:
            login(request,user)
            messages.success(request,'Welcome back')
            return redirect("/user")
        else :
            messages.error(request,'Invalid username or password')
            return redirect("/user/login")
    return render(request,'login.html')

def logoutUser(request):
    logout(request)
    return redirect("/user/login")
