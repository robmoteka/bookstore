from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Publisher,Book,Author, BookCategory



class BookListView(ListView):
    model = Book

class BookDetailView(DetailView):
    model = Book

class AuthorListView(ListView):
    model = Author

class PublisherListView(ListView):
    model = Publisher

class AuthorDetailView(DetailView):
    model = Author

class BookCategoryDetailView(DetailView):
    model = BookCategory