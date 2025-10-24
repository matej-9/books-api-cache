from django.db import models

RATING = [(number, str(number)) for number in range(6)]

class Author(models.Model):
    name = models.CharField(unique=True, max_length=256)

class Book(models.Model):
    title = models.CharField(unique=True, max_length=256)
    authors = models.ManyToManyField(Author, related_name='books')
    year = models.PositiveSmallIntegerField()
    rating = models.IntegerField(choices=RATING)
    review = models.TextField(max_length=1024, null=True, blank=True)

