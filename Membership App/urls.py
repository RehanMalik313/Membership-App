from django.urls import path
from . import views

urlpatterns = [
   path('', views.join, name="join"),
   path('home', views.home, name='home'),
]