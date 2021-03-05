from django import forms
from .models import Article
from .models import Customer
class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ["title","content","article_image",]

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'
        exclude = ['user']