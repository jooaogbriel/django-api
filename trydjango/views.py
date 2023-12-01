"""
To render html web pages
"""
import random
from django.http import HttpResponse

from articles.models import Article


def home_view(request):
    """
    Take in a request (Django sends request)
    Return HTML as a response (We pick to return the response)
    """
    # from the database??
    article_obj = Article.objects.get(title='try python')

    # Django Templates
    H1_STRING = f"""
    <h1>{article_obj.title}
    """
    P_STRING = f"""
    <p>{article_obj.content}!</p>
    """
    HTML_STRING = H1_STRING + P_STRING
    return HttpResponse(HTML_STRING)