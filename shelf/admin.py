from .models import Author, Publisher, Book
from django.contrib import admin

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    search_fields = ['first_name', 'second_name']
    ordering = ['-first_name']

@admin.register(Publisher)
class PublisherAdmin(admin.ModelAdmin):
    search_fields = ['name']


class BookAdmin(admin.ModelAdmin):
    search_fields = ['title', 'author']
    list_display = ['title', 'author' ,'isbn']
    ordering = ['title']



admin.site.register(Book, BookAdmin)
