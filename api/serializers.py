from rest_framework import serializers
from .models import Book, User

class BookSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Book
        fields = '_all_'

class UserSerializer(serializers.ModelSerializer):
    book = BookSerializer(many=True)

    class Meta:
        model = User
        fields = ['name', 'book']

