from django.contrib import admin
from django.urls import path,include
from article import views
app_name = "article"

urlpatterns = [
    path("dashboard/",views.dashboard,name="dashboard"),
    path("dashboard2/",views.dashboard2,name="dashboard2"),
    path("article/<int:id>",views.detail,name="detail"),
]