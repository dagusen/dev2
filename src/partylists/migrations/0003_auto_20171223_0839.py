# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-23 08:39
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('partylists', '0002_auto_20171223_0838'),
    ]

    operations = [
        migrations.AlterField(
            model_name='partylist',
            name='goals',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='partylist',
            name='projects',
            field=models.TextField(default=django.utils.timezone.now, help_text=b'seperate each item by comma'),
            preserve_default=False,
        ),
    ]
