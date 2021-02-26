from django.shortcuts import render,redirect

#Modeller
from .forms import RegisterForm,LoginForm
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate,logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages



def register(request):
    form = RegisterForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        newUser = User(username = username)
        newUser.set_password(password)

        newUser.save()
        login(request,newUser)
        messages.info(request,"Başarıyla Kayıt Olundu")

        return redirect("index")
    context = {
        "form":form
    }

    return render(request,"register.html",context)

def loginUser(request):
    return render(request,"login.html")

def logoutUser(request):
    return render(request,"logout.html")