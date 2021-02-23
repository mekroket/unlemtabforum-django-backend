from django.db import models
#ck editör
from ckeditor.fields import RichTextField
# Create your models here.

#makale oluşturma
class Article(models.Model):
    author = models.ForeignKey("auth.User",on_delete= models.CASCADE,verbose_name="Yazar")
    title = models.CharField(max_length=50,verbose_name="Başlık")
    content = models.TextField()
    created_date= models.DateTimeField(auto_now=True,verbose_name="Oluşturma Tarihi")
    article_image = models.FileField(blank=True,null=True,verbose_name="Resim Ekle")


    #başlık gösterme
    def __str__(self):
        return self.title
    
