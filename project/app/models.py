from django.db import models

# Create your models here.
# creating model for author
class Author(models.Model):
    name=models.CharField(max_length=100)
    email= models.EmailField()
    def __str__(self) -> str:
        return self.name
# creating model for Blog Posts
class BlogPost(models.Model):
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=100)
    publication_date=models.DateField()
    author = models.ForeignKey(Author  , on_delete=models.CASCADE)
    def __str__(self) -> str:
        return self.title
    
class UserAuthentication(models.Model):
    userName = models.CharField(max_length=100)
    password = models.CharField(max_length=100)