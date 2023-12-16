from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('api/', include('sulfur.urls')),
    path('', include('sulfur.urls')),
    path('admin/', admin.site.urls),
]
