from django.conf.urls import url
from django.contrib import admin
from core import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^contato/', views.contato, name='contato'),
    url(r'^sobre/', views.sobre, name='sobre'),
    url(r'^admin/', admin.site.urls),
]
