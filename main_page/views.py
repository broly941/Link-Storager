import operator
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from .models import Links, Tags
from .forms import LinksForm

import requests
import json

GOOGLE_URL_SHORTEN_API = 'AIzaSyCeZMN-uyaLrbEACHreeLJLFzGBi2LvoJY'

def main_page(request):
    links = Links.objects.all()
    ordered_links = sorted(links, key=operator.attrgetter('created_date'), reverse=True)
    return render(request, 'main_page/main_page.html', locals())


def create_link(request):
    tags = Tags.objects.all()
    ordered_tags = sorted(tags, key=operator.attrgetter('name'))

    form = LinksForm(request.POST)
    if form.is_valid():
        link = form.save(commit=False)

        link.author = request.user
        link.shortcut = google_url_shorten(form.cleaned_data['original'])
        link.created_date = timezone.now()
        link.save()
        return redirect('links_detail', pk=link.pk)
    else:
        form = LinksForm()
    return render(request, 'main_page/create_link.html', locals())


def tags(request):
    tags = Tags.objects.all()
    ordered_tags = sorted(tags, key=operator.attrgetter('name'))

    return render(request, 'main_page/tags.html', locals())


def tags_detail(request, pk):
    tags = get_object_or_404(Tags, pk=pk)
    links = Links.objects.all()
    return render(request, 'main_page/tags_detail.html', locals())


def links_detail(request, pk):
    links = get_object_or_404(Links, pk=pk)
    return render(request, 'main_page/links_detail.html', locals())

def google_url_shorten(url):
   req_url = 'https://www.googleapis.com/urlshortener/v1/url?key=' + GOOGLE_URL_SHORTEN_API
   payload = {'longUrl': url}
   headers = {'content-type': 'application/json'}
   r = requests.post(req_url, data=json.dumps(payload), headers=headers)
   resp = json.loads(r.text)
   return resp['id']

