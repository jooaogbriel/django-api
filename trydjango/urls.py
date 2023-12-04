from django.urls import path
from articles.views import ArticlesViews

urlpatterns = [
    path('api/articles/', ArticlesViews.as_view()), # index / home / root
]