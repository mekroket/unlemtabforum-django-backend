from django.shortcuts import render,HttpResponse,redirect,get_object_or_404
from .models import Article,Comment
from .forms import ArticleForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required


from forum import urls
# Create your views here.


def index(request):
    return render(request,"index.html")

def about(request):
    return render(request,"about.html")



def detail(request,id):
    article = get_object_or_404(Article,id=id)
    comments = article.comments.all()

    return render(request,"detail.html",{"article":article,"comments":comments})


def news(request):
    return render(request,"news.html")


def addcomment(request,id):
    article = get_object_or_404(Article,id=id)
    if request.method == "POST":
        comment_author = request.POST.get("comment_author")
        comment_content = request.POST.get("comment_content")

        newComment = Comment(comment_author=comment_author,comment_content=comment_content)

        newComment.article = article

        newComment.save()
    return redirect("/articles/article/" + str(id))







@login_required(login_url="user:login")
def addarticle(request):
    form = ArticleForm(request.POST or None,request.FILES or None)

    if form.is_valid():
        article = form.save(commit=False)
        
        article.author = request.user
        article.save()

        messages.success(request,"Makale başarıyla oluşturuldu")
        return redirect("article:articles")
    return render(request,"addarticle.html",{"form":form})


#######################################################


    

def articles2(request):
    if request.user.is_authenticated == False:
        articles = Article.objects.all()
        return render(request,"articles2.html",{"articles":articles})
    return render(request,"articles2.html")


def articles(request):
    if request.user.is_authenticated == False:
        return redirect("/articles/articles2")
        messages.error(request,"Projelere Erişmek İçin Lütfen Giriş Yapınız")
        
    if request.user.is_authenticated == True:
        articles = Article.objects.all()
        return render(request,"articles.html",{"articles":articles})

    else:
        articles = Article.objects.all()
        articles = Article.objects.filter(author=request.user)
        context = {
            "articles":articles,
        }
    
    return render(request,"articles.html",context)


@login_required(login_url = "user:login")
def dashboard(request):
    articles = Article.objects.filter(author=request.user)
    context = {
        "articles":articles
    }
    return render(request,"dashboard.html",context)

@login_required(login_url = "user:login")
def update(request,id):
    article = get_object_or_404(Article, id = id)
    form = ArticleForm(request.POST or None, request.FILES,instance=article)
    if form.is_valid():
        article = form.save(commit=False)

        article.author = request.user
        article.save()
        messages.success(request,"Makale Başarıyla Güncellendi")
        return redirect("articles/dashboard")
    return render(request,"update.html", {"form":form})

def delete(request,id):
    article = get_object_or_404(Article,id = id)
    article.delete()
    messages.success(request,"Makaleniz Başarıyla Silindi")
    return redirect("/articles/dashboard")
    
