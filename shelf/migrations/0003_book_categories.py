# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-03-23 08:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shelf', '0002_auto_20180322_1947'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='categories',
            field=models.ManyToManyField(to='shelf.BookCategory'),
        ),
    ]
