# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-06-01 16:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('twitter_blocker', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='user_id',
            field=models.IntegerField(unique=True),
        ),
    ]
