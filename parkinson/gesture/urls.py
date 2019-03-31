# from django.urls import path
from gesture import views
from django.conf.urls import include, url
app_name="gesture"
urlpatterns = [
    url(r'handwriting', views.handwriting, name='handwriting'), 
    url(r'sleep', views.sleep, name='sleep'), 
    url(r'well', views.sleepwell, name='well'), 
    url(r'movement', views.movement, name='movement'),
    url(r'alert', views.sms, name='sms'),
    url(r'safe', views.safe, name='safe'),
    url(r'emergency', views.emergency, name='emergency'),
    url(r'success', views.send, name='send'),  
]