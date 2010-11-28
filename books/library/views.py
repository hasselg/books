from django.conf import settings
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.utils import simplejson
from django.views.decorators.csrf import csrf_protect

from books.library.models import Book, BookModelForm, Author, AuthorModelForm

def homepage(request):
    # Get the last 5 read books
    last_five_books = Book.objects.order_by('year_read').reverse()[:5]
    context = {
        'last_five_books': last_five_books}
    return render_to_response('library/index.html', context)

@csrf_protect
def edit_book(request, book_id=None):
    if book_id is not None:
        try:
	        book = Book.objects.get(pk=book_id)
        except Book.DoesNotExist:
            book = None
    else:
        book = None

    if request.method == 'POST':
        book_form = BookModelForm(request.POST, instance=book)
        if book_form.is_valid():
            book = book_form.save()
            return HttpResponseRedirect(reverse('books.library.views.edit_book', args=(book.id,)))
    else:
        book_form = BookModelForm(instance=book)

    author_form = AuthorModelForm(instance=None)

    return render_to_response('library/book_detail.html', {'book_form': book_form, 'author_form': author_form}, context_instance=RequestContext(request))

@csrf_protect
def add_author_ajax(request):
    if request.method == 'POST':
        if request.is_ajax():
            form = AuthorModelForm(request.POST)
            if form.is_valid():
                author = form.save()
                message = simplejson.dumps({'pk': author.id, 'author': str(author)}, ensure_ascii=False)

                return HttpResponse(message, mimetype='application/javascript')
            else:
                print "form is not valid"
                print form.errors

        else:
            message = "Hello"
            return HttpResponse(message)

@csrf_protect
def edit_author(request, author_id=None):
    if author_id is not None:
        try:
            author = Author.objects.get(pk=author_id)
            books = author.book_set.all()
        except Author.DoesNotExist:
            author = None
            books = None
    else:
        author = None
        books = None

    if request.method == 'POST':
        form = AuthorModelForm(request.POST, instance=author)
        if form.is_valid():
            author = form.save()
            return HttpResponseRedirect(reverse('books.library.views.edit_author', args=(author.id,)))
    else:
        form = AuthorModelForm(instance=author)

    return render_to_response('library/author_detail.html', {'form': form, 'books': books}, context_instance=RequestContext(request))

