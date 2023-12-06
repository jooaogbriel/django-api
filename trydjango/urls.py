# from django.urls import path
# from articles.views import BlogPostListCreateView, CommentListCreateView, CommentDetailView
# from articles.views import custom_blog_view, custom_blog_detail

# urlpatterns = [
#     path('blog/', custom_blog_view, name='blog-post-list'),
#     path('blog/<int:pk>/', custom_blog_detail, name='blog-post-detail'),
#     path('comments/', CommentListCreateView.as_view(), name='comment-list'),
#     path('comments/<int:pk>/', CommentDetailView.as_view(), name='comment-detail'),
# ]

# urls.py
from django.urls import path
from articles.views import (
    BlogPostListCreateView,
    BlogPostDetailView,
    CommentListCreateView,
    CommentDetailView,
    CustomBlogView,
    CustomBlogDetailView
)

urlpatterns = [
    path('api/blog/', BlogPostListCreateView.as_view(), name='blog-post-list'),
    path('api/blog/<int:pk>/', BlogPostDetailView.as_view(), name='blog-post-detail'),
    path('api/comments/', CommentListCreateView.as_view(), name='comment-list'),
    path('api/comments/<int:pk>/', CommentDetailView.as_view(), name='comment-detail'),
    path('blog/', CustomBlogView.as_view(), name='custom-blog-view'),
    path('blog/<int:pk>/', CustomBlogDetailView.as_view(), name='custom-blog-detail'),
]
