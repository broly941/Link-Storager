import operator
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .models import Links, Tags
from .forms import LinksForm, UserLoginForm
from main_page.google_api import google_url_shorten
from django.contrib.auth import (
    authenticate,
    get_user_model,
    login,
    logout
    )


def main_page(request):
    links = Links.objects.all()
    ordered_links = sorted(links, key=operator.attrgetter('created_date'), reverse=True)
    return render(request, 'main_page/main_page.html', locals())

# @login_required(login_url='/login/')
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
    links = Links.objects.all()
    return render(request, 'main_page/tags_detail.html', locals())


def links_detail(request, pk):
    links = get_object_or_404(Links, pk=pk)
    return render(request, 'main_page/links_detail.html', locals())


def login_view(request):
    title = 'Авторизация'
    form = UserLoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        login(request, user)
    return render(request, 'main_page/login.html', locals())

def register_view(request):
    return render(request, 'main_page/', locals())

def logout_view(request):
    return render(request, 'main_page/login.html', locals())

