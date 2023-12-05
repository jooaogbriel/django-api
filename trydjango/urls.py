from django.urls import path
from articles.views import BlogPostListCreateView, BlogPostDetailView, CommentListCreateView, CommentDetailView
from articles.views import custom_blog_view 

urlpatterns = [
    path('blog/', custom_blog_view, name='blog-post-list'),
    path('blog/<int:pk>/', BlogPostDetailView.as_view(), name='blog-post-detail'),
    path('comments/', CommentListCreateView.as_view(), name='comment-list'),
    path('comments/<int:pk>/', CommentDetailView.as_view(), name='comment-detail'),
]