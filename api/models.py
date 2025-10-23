from django.db import models

class Book(models.Model):
    title = models.CharField(unique=True, max_length=256, null=False, blank=False)
    author = models.CharField(max_length=256, null=False, blank=False)
    year = models.PositiveSmallIntegerField()
    rating = models.IntegerField()
    review = models.TextField(max_length=1024, null=True)

class User(models.Model):
    name = models.CharField(unique=True, max_length=256, null=False, blank=False)
    password = models.CharField(max_length=12)
    books = models.ManyToManyField(Book, related_name='user')

