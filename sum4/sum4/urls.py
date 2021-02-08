
from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('cals.urls')),
    path('aboutus/',include('aboutus.urls')),
    path('contact/',include('contact.urls')),
    path('authentication/',include('authentication.urls')),
    path('employee/',include('employee.urls')),
    path('clientus/',include('clientus.urls')),
    path('portfulio/',include('portfulio.urls')),
 
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
