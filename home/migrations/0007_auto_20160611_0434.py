# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-10 23:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_auto_20160611_0434'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='mobile_number',
            field=models.IntegerField(),
        ),
    ]
