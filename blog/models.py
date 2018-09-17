from django.db import models

from django.urls import reverse

"""
This is Article model
"""
class Article(models.Model):
    title = models.CharField(max_length=200)
    abstract = models.CharField(max_length=500)
    time = models.DateTimeField()
    description = models.TextField()
    author_name = models.CharField(max_length=100)

    def get_absolute_url(self):
        return reverse("articles:article-detail", kwargs={"id" : self.id})
    #Explanation
    # here articles is the name of the folder
    # # articles-detail is the name defined in the urls
    