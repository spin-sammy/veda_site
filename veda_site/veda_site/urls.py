from django.contrib import admin
from django.urls import path, include

from veda.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('veda.urls')),
    path('games/', include('games.urls')),
]

