# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-21 08:52
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0022_auto_20160621_1344'),
    ]

    operations = [
        migrations.RenameField(
            model_name='disableddates',
            old_name='did',
            new_name='id',
        ),
    ]
