from rest_framework import serializers
from .models import Book, Author, Times

class AuthorSerializer(serializers.ModelSerializer):
    """Serializer for Author"""
    books = serializers.SlugRelatedField(slug_field='title', read_only=True, many= True)
    class Meta:
        model = Author
        fields = ['name', 'books']

class BookSerializer(serializers.ModelSerializer):
    """Serializer for Book"""
    authors = serializers.SlugRelatedField(slug_field='name', read_only=True, many= True)

    class Meta:
        model = Book
        fields = '__all__'

class TimeSerializer(serializers.ModelSerializer):
    """Serializer for Time measured during requests"""
    class Meta:
        model = Times
        fields = '__all__'


