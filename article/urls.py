from django.contrib import admin
from django.urls import path,include
from article import views
app_name = "article"

urlpatterns = [
    path("dashboard/",views.dashboard,name="dashboard"),
    path("article/<int:id>",views.detail,name="detail"),
]