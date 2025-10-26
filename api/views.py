from django.shortcuts import render
import time
from functools import wraps
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import RetrieveAPIView
from .models import Book, Author, Times
from .serializers import BookSerializer, AuthorSerializer, TimeSerializer
from rest_framework import status
from .scripts import graph, simulation


# Decorator for measuring time of the requests and saving it into the DB as Times model#
def performance_timer(func):
    """Decorator for measuring time of the requests and saving it into the DB as Times model"""
    def wrapper(self, request,*args, **kwargs):
        time_start = time.time()
        result = func(self, request,*args, **kwargs)
        time_finish = time.time()
        total_time = time_finish - time_start

        Times.objects.create(
            method = request.method,
            time=total_time
        )

        return result
    return wrapper

class BookList(APIView):
    """View for Book List (all books from DB)"""
    @performance_timer
    def get(self, request):
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data, template_name= 'api.html')
    def post(self, request):
        serializer = BookSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)


class BookDetail(RetrieveAPIView):
    """View for Book detail/specific book acc. to PK"""
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class AuthorList(APIView):
    """View for Author List (all authors from DB)"""
    @performance_timer
    def get(self, request):
        author = Author.objects.all()
        serializer = AuthorSerializer(author, many = True)
        return Response(serializer.data)
    
class TimeList(APIView):
    """View for Times measured by our decorator for each request decorated"""
    def get(self, request):
        times = Times.objects.all()
        serializer = TimeSerializer(times, many = True)
        return Response(serializer.data)
    
class AuthorDetail(RetrieveAPIView):
    """View for Book detail/specific book acc. to PK"""
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

def graph_view(request):
    get_graph = graph.getting_graph()
    if get_graph == None:
        context = 'No data to show! Please run simulation!'
        return render(request, context)
    elif request.method == 'POST' and request.POST.get('action') == 'cache':
        number_str = int(request.POST.get('my_number'))
        simulation.sending_requests(number_str)
        get_graph = graph.getting_graph()
        context = {'graph_base64': get_graph}
        return render(request, 'rest_framework/graph.html', context)
    elif request.method == 'POST' and request.POST.get('action') == 'reset':
        simulation.reset_db()
        get_graph = graph.getting_graph()
        context = {'graph_base64': get_graph}
        return render(request, 'rest_framework/graph.html', context)
    else:
        context = {'graph_base64': get_graph}
        return render(request, 'rest_framework/graph.html', context)

