# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-18 20:28
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0005_auto_20161218_2203'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job_place',
            name='j_name',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main_app.Organisation', verbose_name='Организация'),
        ),
    ]