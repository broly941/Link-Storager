from django.contrib import admin
from .models import *


class LinksAdmin(admin.ModelAdmin):
    list_display = ["id", "original", "description"]

    list_filter = ['tag', 'created_date']

    search_fields = ['tag', 'original', 'shortcut']

    class Meta:
        model = Links

admin.site.register(Links, LinksAdmin)


class TagsAdmin(admin.ModelAdmin):
    list_display = ['name']

    search_fields = ['name']

    class Meta:
        model = Tags

admin.site.register(Tags, TagsAdmin)
