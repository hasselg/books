from django.conf import settings
from django.shortcuts import render_to_response

def homepage(request):
    context = {'MEDIA_URL': settings.MEDIA_URL}
    return render_to_response('library/index.html', context)


