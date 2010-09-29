from django.conf import settings
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.views.decorators.csrf import csrf_protect

from books.library.models import Book, BookModelForm

def homepage(request):
    # Get the last 5 read books
    last_five_books = Book.objects.order_by('year_read').reverse()[:5]
    context = {
        'last_five_books': last_five_books}
    return render_to_response('library/index.html', context)

@csrf_protect
def edit_book(request, book_id=None):
    if book_id is not None:
	book = Book.objects.get(pk=book_id)
    else:
        book = None

    if request.method == 'POST':
        form = BookModelForm(request.POST, instance=book)
	if form.is_valid():
            form.save()
    else:
        form = BookModelForm(instance=book)

    return render_to_response('library/detail.html', {'form': form}, context_instance=RequestContext(request))

