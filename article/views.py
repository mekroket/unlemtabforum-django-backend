from django.shortcuts import render,HttpResponse,redirect,get_object_or_404
from .models import Article
from .forms import ArticleForm
from django.contrib import messages
# Create your views here.


def index(request):
    return render(request,"index.html")

def about(request):
    return render(request,"about.html")

def dashboard(request):
    if request.user.is_authenticated == False:
        return redirect("dashboard2")
        messages.error(request,"Projelere Erişmek İçin Lütfen Giriş Yapınız")
        
    else:

        articles = Article.objects.filter(author=request.user)
        context = {
            "articles":articles,
        }
    
    return render(request,"dashboard.html",context)

def detail(request,id):
    article = get_object_or_404(Article,id=id)
    return render(request,"detail.html",{"article":article})


def news(request):
    return render(request,"news.html")

def dashboard2(request):
    return render(request,"dashboard2.html")

def addarticle(request):
    return render(request,"addarticle.html")

def articles(request):
    articles = Article.objects.all()
    return render(request,"dashboard2.html",{"articles":articles})

def addarticle(request):
    form = ArticleForm(request.POST or None)
    if form.is_valid():
        article = form.save(commit=False)
        article.author = request.user
        article.save()

        messages.success(request,"Makale Başarıyla Oluşturuldu")
        return redirect("dashboard")

    return render(request,"addarticle.html",{"form":form})