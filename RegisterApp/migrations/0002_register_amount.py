# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-24 21:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RegisterApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='register',
            name='amount',
            field=models.IntegerField(default=0),
        ),
    ]