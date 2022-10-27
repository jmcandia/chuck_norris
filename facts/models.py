from django.db import models


# Create your models here.
class Fact(models.Model):
    fact = models.CharField(max_length=400)
    creation_date = models.DateTimeField(auto_now_add=True)
