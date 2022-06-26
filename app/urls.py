from django.urls import path, include
from .views import home

app_name = 'app'

urlpatterns = [
    path('', home, name='home')
]
