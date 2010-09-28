from django.conf import settings
from django.shortcuts import render_to_response

from books.library.models import Book

def homepage(request):
    # Get the last 5 read books
    last_five_books = Book.objects.order_by('year_read').reverse()[:5]
    context = {
        'last_five_books': last_five_books}
    return render_to_response('library/index.html', context)

