from django.conf.urls import url
from .views import AuthorListView, BookListView, PublisherListView, AuthorDetailView, BookDetailView, BookCategoryDetailView


app_name = "shelf"
urlpatterns = [
    url(r'^authors\/$', AuthorListView.as_view(), name='author-list'),
    url(r'^authors/(?P<pk>\d+)\/$', AuthorDetailView.as_view(), name='author-detail'),
    url(r'^books\/$', BookListView.as_view(), name='book-list'),
    url(r'^books/(?P<pk>\d+)\/$', BookDetailView.as_view(), name='book-detail'),
    url(r'^publishers\/$', PublisherListView.as_view(), name='publisher-list'),
    url(r'^categories/(?P<pk>\d+)\/$', BookCategoryDetailView.as_view(), name='category-detail'),
]

