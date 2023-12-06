# from rest_framework import generics
# from .models import BlogPost, Comment
# from .serializers import BlogPostSerializer, CommentSerializer
# from django.shortcuts import render, get_object_or_404
# from django.shortcuts import render
# from django.http import HttpResponseRedirect
# from .models import BlogPost

# def custom_blog_view(request):
#     posts = BlogPost.objects.all()
#     return render(request, 'blog_post_list.html', {'posts': posts})

# def custom_blog_detail(request):
#     posts = BlogPost.objects.all()
#     return render(request, 'blog_detail', {'posts':posts})

# class BlogPostListCreateView(generics.ListCreateAPIView):
#     queryset = BlogPost.objects.all()
#     template_name = 'templates/blog_post_list.html'
#     serializer_class = BlogPostSerializer

#     template_name = 'articles/article_detail.html'

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         article = get_object_or_404(BlogPost, pk=kwargs['pk'])
#         comments = Comment.objects.filter(article=article)

#         context['article'] = article
#         context['comments'] = comments
#         return context

#     def post(self, request, *args, **kwargs):
#         article = get_object_or_404(BlogPost, pk=kwargs['pk'])
        
#         # Lógica para adicionar um novo comentário
#         name = request.POST['name']
#         email = request.POST['email']
#         body = request.POST['body']

#         Comment.objects.create(article=article, name=name, email=email, body=body)

#         # Redireciona de volta para a página do post após adicionar o comentário
#         return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

# class CommentListCreateView(generics.ListCreateAPIView):
#     queryset = Comment.objects.all()
#     serializer_class = CommentSerializer

# class CommentDetailView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Comment.objects.all()
#     serializer_class = CommentSerializer

# views.py
from rest_framework import generics
from .models import BlogPost, Comment
from .serializers import BlogPostSerializer, CommentSerializer
from django.shortcuts import render, get_object_or_404
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.generic import TemplateView

class BlogPostListCreateView(generics.ListCreateAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer

class BlogPostDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer

    def post(self, request, *args, **kwargs):
        instance = self.get_object()
        # Lógica para adicionar um novo comentário
        name = request.data.get('name')
        email = request.data.get('email')
        body = request.data.get('body')

        Comment.objects.create(article=instance, name=name, email=email, body=body)

        return self.retrieve(request, *args, **kwargs)

class CommentListCreateView(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

class CommentDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

class CustomBlogView(TemplateView):
    template_name = 'blog_post_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts'] = BlogPost.objects.all()
        return context

class CustomBlogDetailView(TemplateView):
    template_name = 'blog_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['post'] = get_object_or_404(BlogPost, pk=kwargs['pk'])
        context['comments'] = Comment.objects.filter(post=context['post'])
        return context

    def post(self, request, *args, **kwargs):
        article = get_object_or_404(BlogPost, pk=kwargs['pk'])
        
        # Lógica para adicionar um novo comentário
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        body = request.POST.get('body', '')

        Comment.objects.create(post=article, name=name, email=email, body=body)

        # Redireciona de volta para a página do post após adicionar o comentário
        return HttpResponseRedirect(request.path)