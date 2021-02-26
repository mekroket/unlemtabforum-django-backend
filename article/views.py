from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request,"index.html")

def about(request):
    return render(request,"about.html")

def articles(request):
    return render(request,"articles.html")

