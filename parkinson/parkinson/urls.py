from django.contrib import admin
# from django.urls import path
import gesture.views
import accounts.views
from django.conf.urls import include, url
#to get images
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', gesture.views.landing),
    url(r'^accounts/', include('accounts.urls')),
    url(r'^gesture/', include('gesture.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
