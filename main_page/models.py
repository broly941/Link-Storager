from django.db import models
from django.utils import timezone
from django.conf import settings


class Tags(models.Model):
    name = models.CharField(max_length=64, default=None)

    def get_links(self):
        return self.links_set.all()

    def __str__(self):
        return "%s" % self.name

    class Meta:
        verbose_name = 'Tag'
        verbose_name_plural = 'Tags'


class Links(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, default=1)
    original = models.CharField(max_length=200)
    shortcut = models.CharField(max_length=200)
    description = models.TextField()
    tag = models.ForeignKey(Tags, blank=True, null=False, default=None)
    created_date = models.DateTimeField(default=timezone.now)

    def get_tags(self):
        return self.tag_id

    def __str__(self):
        return self.original

    class Meta:
        verbose_name = 'Link'
        verbose_name_plural = 'Links'
