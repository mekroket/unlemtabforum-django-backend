#FORMLAR BURAYA GİRİLİYOR
#KAYIT FORMLARI
from django import forms #önce form modülünü import ediyoruz
from django.contrib.auth.models import User

#kayıt formu
class RegisterForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(
        attrs={"class":"input-text","placeholder":"Kullanıcı Adı"}
    ),required=True,max_length=50)

    password = forms.CharField(widget=forms.PasswordInput(
        attrs={"class":"input-text","placeholder":"Şifre"}
    ))
    
    email = forms.CharField(widget=forms.EmailInput(
        attrs={"class":"input-text","placeholder":"Email"}
    ),required=True,max_length=50)

    class Meta():
        model = User
        fields = ["username","email","password"]

    def clean(self):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")
        
        values = {
            "username":username,
            "password":password
        }
        return values

#GİRİŞ YAPMA
class LoginForm(forms.Form):
    username = forms.CharField(label="Kullanıcı Adı")
    password = forms.CharField(label="Şifre",widget=forms.PasswordInput)
