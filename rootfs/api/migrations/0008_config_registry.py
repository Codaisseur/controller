# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-21 19:06
from __future__ import unicode_literals

from django.db import migrations
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_auto_20160226_2335'),
    ]

    operations = [
        migrations.AddField(
            model_name='config',
            name='registry',
            field=jsonfield.fields.JSONField(blank=True, default={}),
        ),
    ]