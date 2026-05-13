from django.contrib import admin
from django.urls import path
from store.views import index, home, catalog, contact, gallery, support, about, login

urlpatterns = [
    path('', index, name='root'),
    path('admin/', admin.site.urls),
    path('index/', index, name='index'),
    path('home/', home, name='home'),
    path('catalog/', catalog, name='catalog'),
    path('contact/', contact, name='contact'),
    path('gallery/', gallery, name='gallery'),
    path('support/', support, name='support'),
    path('about/', about, name='about'),
    path('login/', login, name='login'),
]