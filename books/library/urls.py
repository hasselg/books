from django.conf.urls.defaults import *
from books.library.models import Author, Book

books_dict = {
    'queryset': Book.objects.all(),
}

authors_dict = {
    'queryset': Author.objects.all(),
}

urlpatterns = patterns('',
    (r'^$',                 'books.library.views.homepage'),
    (r'^create_book/$',     'books.library.views.edit_book'),
    (r'^edit_book/(\d+)/$', 'books.library.views.edit_book'),
    (r'^list_books/$',      'django.views.generic.list_detail.object_list', books_dict),

    (r'^create_author_ajax/$',  'books.library.views.add_author_ajax'),
    (r'^create_author/$',       'books.library.views.edit_author'),
    (r'^edit_author/(\d+)/$',   'books.library.views.edit_author'),
    (r'^list_authors/$',        'django.views.generic.list_detail.object_list', authors_dict),
)

