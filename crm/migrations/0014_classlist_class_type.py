# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-12-23 07:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0013_auto_20161223_0445'),
    ]

    operations = [
        migrations.AddField(
            model_name='classlist',
            name='class_type',
            field=models.SmallIntegerField(choices=[(0, '面授'), (1, '随到随学网络')], default=0),
        ),
    ]
