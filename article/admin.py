from django.contrib import admin
#
from .models import Article,Comment,Customer

# Register your models here.

admin.site.register(Comment)
admin.site.register(Customer)




@admin.register(Article)        #bu komutla adminde gösteriyoruz
class articleadmin(admin.ModelAdmin):
    list_display = ["title","author","created_date"] #makale ekleme yerindekileri isimlerini düzenlemeye yarıyor
    list_display_links = ["title","created_date"]  #buda makale ekleme yerindekilere link veriyo

    search_fields = ["title"] #makale kısmında arama yapmayı sağlıyor

    list_filter = ["created_date"]#makale panelinde tarihleri sıralama işlevini görüyor sıralama yapıyor

    class Meta: #yapılması zorunlu class
        model = Article