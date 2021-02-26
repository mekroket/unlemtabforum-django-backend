#KAYIT FORMLARI BU KISMA GİRİLİYOR
#KAYIT FORMLARI
from django import forms
from django.contrib.auth.forms import AuthenticationForm
from user import urls
from django.contrib.auth.models import User


class RegisterForm(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput(
        attrs={"class": "input-text","placeholder":"Kullanıcı Adı"}
    ),required=True,max_length=50)

    email = forms.CharField(widget=forms.EmailInput(
        attrs={"class":"input-text","placeholder":"Email"}
    ),required=True,max_length=50)

    password = forms.CharField(widget=forms.PasswordInput(
        attrs={"class":"input-text","placeholder":"Şifre"}
    ),required=True,max_length=50)

    class Meta():
        model = User
        fields = ["username","email","password"]

    def clean(self):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")
        email = self.cleaned_data.get("email")

        values = {
            "username" : username,
            "password" : password,
            "email":email,
            
        }
        return values

class LoginForm(forms.Form):
    username = forms.CharField(label = "Kullanıcı Adı")
    password = forms.CharField(label = "Parola",widget = forms.PasswordInput)
