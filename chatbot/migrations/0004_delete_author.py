# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-04-19 12:46
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chatbot', '0003_author'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Author',
        ),
    ]