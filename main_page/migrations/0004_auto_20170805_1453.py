# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-05 11:53
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_page', '0003_auto_20170805_1414'),
    ]

    operations = [
        migrations.AlterField(
            model_name='links',
            name='author',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='links',
            name='tag',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='main_page.Tags'),
        ),
    ]