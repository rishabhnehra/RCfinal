# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-10 23:12
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_auto_20160611_0434'),
    ]

    operations = [
        migrations.RenameField(
            model_name='booking',
            old_name='booked_date',
            new_name='timestamp',
        ),
    ]
