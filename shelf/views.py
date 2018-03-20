from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Publisher,Book,Author

class BookListView(ListView):
    model = Book

class AuthorListView(ListView):
    model = Author

class PublisherListView(ListView):
    model = Publisher

class AuthorDetailView(DetailView):
    model = Author