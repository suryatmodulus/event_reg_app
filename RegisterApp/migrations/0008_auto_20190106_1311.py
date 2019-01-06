# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2019-01-06 07:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RegisterApp', '0007_auto_20190106_1210'),
    ]

    operations = [
        migrations.RenameField(
            model_name='register',
            old_name='registd_date',
            new_name='reg_date',
        ),
        migrations.AddField(
            model_name='register',
            name='reg_by',
            field=models.CharField(default=0, max_length=100),
        ),
        migrations.AlterField(
            model_name='register',
            name='college_name',
            field=models.CharField(max_length=150),
        ),
    ]