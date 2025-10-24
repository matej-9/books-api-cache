from rest_framework import serializers
from .models import Book, Author

class AuthorSerializer(serializers.ModelSerializer):
    books = serializers.SlugRelatedField(slug_field='title', read_only=True, many= True)
    class Meta:
        model = Author
        fields = ['name', 'books']

class BookSerializer(serializers.ModelSerializer):
    authors = serializers.SlugRelatedField(slug_field='name', read_only=True, many= True)

    class Meta:
        model = Book
        fields = '__all__'


