from django.conf.urls import include, url
from . import views

app_name = 'accounts'

urlpatterns = [
    url(r'^signup', views.signup, name='signup'), 
    url(r'^login', views.loginview, name='login'), 
]