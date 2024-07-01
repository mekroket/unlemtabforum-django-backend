# Unlemtab Forum Django Backend

Bu proje, Django ve SQLite kullanılarak geliştirilmiş bir forum sitesi uygulamasıdır. Kullanıcıların üye olabileceği, soru sorabileceği, cevap verebileceği, yorum yapabileceği ve profil bilgilerini düzenleyebileceği bir platform sunar.

## Kurulum ve Çalıştırma Adımları

### 1. Projeyi Klonlayın ve Bağımlılıkları Yükleyin

```bash
git clone https://github.com/mekroket/unlemtabforum-django-backend.git
cd unlemtabforum-django-backend
pip install -r requirements.txt

python manage.py migrate

python manage.py collectstatic
python manage.py createsuperuser

Ek Bilgiler
Projeyi çalıştırmak için Python 3 ve pip kurulu olmalıdır.
Django ve diğer bağımlılıkların sürümleri requirements.txt dosyasında belirtilmiştir.
Daha fazla bilgi için Django Dokümantasyonunu ziyaret edebilirsiniz.
