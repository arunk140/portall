from django.shortcuts import redirect, get_object_or_404, render
from django.http import HttpResponse
from .models import Shortcut
import re

def formaturl(url):
    if not re.match('(?:http|ftp|https)://', url):
        return 'https://{}'.format(url)
    return url

def index(request):
    shortcut_list = Shortcut.objects.order_by('-category')
    context = {'shortcut_list': shortcut_list}
    return render(request, 'home/index.html', context)
    # return HttpResponse("Hello, world. You're at the Shortcuts index.")

def redir(request, shortcut_id):
    shortc = get_object_or_404(Shortcut, pk=shortcut_id)
    return redirect(formaturl(shortc.url_path))