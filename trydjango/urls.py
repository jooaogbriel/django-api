from django.urls import path
from trydjango import views

urlpatterns = [
    path('', views.home_view, name='home'), # index / home / root
]