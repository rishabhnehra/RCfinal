# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-10 09:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20160610_0301'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookings',
            name='message',
            field=models.CharField(max_length=250),
        ),
    ]
