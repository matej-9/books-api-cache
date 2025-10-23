from django.urls import path, include
from . import views

urlpatterns = [
    path("",views.BookList.as_view(), name='books'),
    path("books/",views.BookList.as_view(), name='books'),
]