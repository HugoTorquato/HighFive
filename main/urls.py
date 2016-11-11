from django.conf.urls import url,include
from . import views
urlpatterns = [
    url(r'^$',views.index, name = 'index'),
    url(r'^index.html', views.index),
    url(r'^about.html',views.about, name = 'about'),
    url(r'^services.html',views.services, name = 'about'),
    url(r'^contact.html',views.contact, name = 'about')
]
