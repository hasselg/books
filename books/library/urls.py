from django.conf.urls.defaults import *
from books.library.models import Author, Book
from django.views.generic.list import ListView

urlpatterns = patterns('',
    (r'^$',                 'books.library.views.homepage'),
    (r'^create_book/$',     'books.library.views.edit_book'),
    (r'^edit_book/(\d+)/$', 'books.library.views.edit_book'),
    (r'^list_books/$',      ListView.as_view(queryset=Book.objects.all())),

    (r'^create_author_ajax/$',  'books.library.views.add_author_ajax'),
    (r'^create_author/$',       'books.library.views.edit_author'),
    (r'^edit_author/(\d+)/$',   'books.library.views.edit_author'),
    (r'^list_authors/$',        ListView.as_view(queryset=Author.objects.all())),
)

