from django.urls import path, include
from . import views

urlpatterns = [
    path("",views.BookList.as_view(), name='books'),
    path("books/",views.BookList.as_view(), name='books'),
    path("books/<int:pk>",views.BookDetail.as_view(), name = 'book'),
    path("authors/",views.AuthorList.as_view(), name='authors'),
    path("authors/<int:pk>",views.AuthorDetail.as_view(), name='author'),
    path("times",views.TimeList.as_view(), name = 'times'),
    path('graph/', views.graph_view, name='graph_view'),
]