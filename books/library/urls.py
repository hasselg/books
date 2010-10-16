from django.conf.urls.defaults import *
from books.library.models import Book

info_dict = {
    'queryset': Book.objects.all(),
}

urlpatterns = patterns('',
    (r'^$', 'books.library.views.homepage'),
    (r'^edit_book/(\d+)/$', 'books.library.views.edit_book'),
    (r'^create_book/$', 'books.library.views.edit_book'),
    (r'^edit_author/(\d+)/$', 'books.library.views.edit_author'),
    (r'^create_author/$', 'books.library.views.add_author_ajax'),
    (r'^list/$', 'django.views.generic.list_detail.object_list', info_dict),
)

