# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-18 17:22
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_auto_20161218_2000'),
    ]

    operations = [
        migrations.RenameField(
            model_name='job_place',
            old_name='name',
            new_name='j_name',
        ),
    ]
