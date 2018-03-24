from .models import Author, Publisher, Book, BookCategory, BookItem, BookEdition
from django.contrib import admin

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    search_fields = ['first_name', 'second_name']
    ordering = ['-first_name']

@admin.register(Publisher)
class PublisherAdmin(admin.ModelAdmin):
    search_fields = ['name']

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    search_fields = ['title', 'author']
    list_display = ['title', 'get_author']
    ordering = ['title']
    list_display_links = ['title', 'get_author']
    list_filter = [ 'authors']


@admin.register(BookCategory)
class BookCategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(BookItem)
class BookItemAdmin(admin.ModelAdmin):
    pass

@admin.register(BookEdition)
class BookEditionAdmin(admin.ModelAdmin):
    pass