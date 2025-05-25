# studentrecord/urls.py

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('fields.urls')),
    path('students/', include('fields.urls', namespace='fields')),
]
