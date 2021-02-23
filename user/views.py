from django.shortcuts import render,redirect

#Modeller
from .forms import RegisterForm,LoginForm
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate,logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages



def register(request):
    return render(request,"register.html")

def loginUser(request):
    return render(request,"login.html")

def logoutUser(request):
    return render(request,"logout.html")