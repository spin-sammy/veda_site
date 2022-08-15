from django.urls import path
from .views import *


urlpatterns = [
    path('', main),
    path('test_game/', test_game)
]
