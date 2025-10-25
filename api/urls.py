from django.urls import path, include
from . import views

urlpatterns = [
    path("",views.BookList.as_view(), name='books'),
    path("books/",views.BookList.as_view(), name='books'),
    path("books/<int:pk>",views.BookDetail.as_view(), name = 'book'),
    path("authors/",views.AuthorList.as_view(), name='authors'),
    path("times",views.TimeList.as_view(), name = 'times'),
]