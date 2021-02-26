from django.shortcuts import render,HttpResponse,redirect,get_object_or_404
from .models import Article
# Create your views here.


def index(request):
    return render(request,"index.html")

def about(request):
    return render(request,"about.html")

def dashboard(request):
    articles = Article.objects.filter(author=request.user)
    context = {
        "articles":articles
    }
    return render(request,"dashboard.html",context)

def detail(request,id):
    article = get_object_or_404(Article,id=id)
    return render(request,"detail.html",{"article":article})


