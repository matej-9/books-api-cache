from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Book, User
from .serializers import BookSerializer, UserSerializer
from rest_framework import status

class BookList(APIView):
    def get(self, request):
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)
    def post(self, request):
        serializer = BookSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)


