from django.db import models

# Create your models here.
class Product(models.Model):
    title = models.TextField()
    description  = models.TextField()
    summary = models.TextField()
    price = models.TextField(default="This is cool !!")
    stars = models.TextField(default="10")