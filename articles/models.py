from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.TextField()
    content = models.TextField()

class Account (models.Model):
    name = models.CharField(max_length=100)
    cpf = models.CharField(max_length=11, unique=True)
    email = models.EmailField(unique=True)
    birthdate = models.DateField(null=True)
    is_married = models.BooleanField(default=False)
    
def __repr__(self) -> str:
    return f"{self.title} - {self.content}"