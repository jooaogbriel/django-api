from rest_framework.views import Request, Response, APIView, status

class ArticlesViews(APIView):
    def post(self, req: Request) -> Response:
        return Response({"msg: post criado"}, status.HTTP_201_CREATED)
    
from django.shortcuts import render
from .models import BlogPost, Comment

def blog(request):
    posts = BlogPost.objects.all()
    return render(request, 'blog.html', {'posts': posts})

def about_me(request):
    # Adicione informações sobre você e seus projetos aqui
    return render(request, 'about_me.html')
