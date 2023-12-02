from django.urls import path
from articles import views

urlpatterns = [
    path('', views.home_view, name='home'), # index / home / root
]