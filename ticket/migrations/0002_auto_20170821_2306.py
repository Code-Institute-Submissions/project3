# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-21 22:06
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ticket', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='date',
            field=models.DateField(default=datetime.date.today),
        ),
    ]
