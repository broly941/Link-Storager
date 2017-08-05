import operator

from django.shortcuts import render, redirect, get_object_or_404
from .models import Links, Tags
from .forms import LinksForm


def main_page(request):
    links = Links.objects.all()
    return render(request, 'main_page/main_page.html', locals())


def create_link(request):
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
