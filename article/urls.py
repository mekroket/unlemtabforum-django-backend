from django.contrib import admin
from django.urls import path,include
from article import views
app_name = "article"

urlpatterns = [
    path("articles/",views.articles,name="articles"),
]