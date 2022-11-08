from django.db import models


# Create your models here.
class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)


class Book(models.Model):
    title = models.CharField(max_length=400)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
