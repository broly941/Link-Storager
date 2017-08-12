import operator
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from .models import Links, Tags
from .forms import LinksForm
from main_page.google_api import google_url_shorten
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


def main_page(request):
    links_list = Links.objects.all()
    ordered_links = sorted(links_list, key=operator.attrgetter('created_date'), reverse=True)

    paginator = Paginator(ordered_links, 4)
    page = request.GET.get('page')

    try:
        links = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        links = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        links = paginator.page(paginator.num_pages)

    return render(request, 'main_page/main_page.html', locals())


def create_link(request):
    tags = Tags.objects.all()
    ordered_tags = sorted(tags, key=operator.attrgetter('name'))

    form = LinksForm(request.POST or None)
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
    links_list = Links.objects.filter(tag=pk)

    paginator = Paginator(links_list, 4)
    page = request.GET.get('page')

    try:
        links = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        links = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        links = paginator.page(paginator.num_pages)
    return render(request, 'main_page/tags_detail.html', locals())


def links_detail(request, pk):
    links = get_object_or_404(Links, pk=pk)
    return render(request, 'main_page/links_detail.html', locals())


