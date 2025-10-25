from django.db import models

RATING = [(number, str(number)) for number in range(6)]

class Author(models.Model):
    name = models.CharField(unique=True, max_length=256)

class Book(models.Model):
    title = models.CharField(max_length=256)
    authors = models.ManyToManyField(Author, related_name='books')
    year = models.CharField(max_length=256, null=True)
    rating = models.IntegerField(choices=RATING, null=True)
    review = models.TextField(max_length=1024, null=True, blank=True)

class Times(models.Model):
    method = models.CharField(max_length=256, null=True)
    time = models.DecimalField(decimal_places=4, max_digits=4)

