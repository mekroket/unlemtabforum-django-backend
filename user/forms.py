#FORMLAR BURAYA GİRİLİYOR
#KAYIT FORMLARI
from django import forms #önce form modülünü import ediyoruz

#kayıt formu
class RegisterForm(forms.Form):
    username = forms.CharField(max_length=50,label="Kullanıcı Adı")
    password = forms.CharField(max_length=50,label="Parola",widget=forms.PasswordInput)
    
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
