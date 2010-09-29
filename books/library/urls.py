from django.conf.urls.defaults import *
from books.library.models import Book

info_dict = {
    'queryset': Book.objects.all(),
}

urlpatterns = patterns('',
    (r'^$', 'books.library.views.homepage'),
    (r'^detail/(\d+)/$', 'books.library.views.edit_book'),
    (r'^list/$', 'django.views.generic.list_detail.object_list', info_dict),
)

