# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-11 15:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=254)),
                ('type', models.CharField(choices=[(b'bug', b'bug'), (b'Payment', b'Payment')], default=((b'bug', b'bug'), (b'Payment', b'Payment')), max_length=254)),
                ('content', models.TextField()),
                ('date', models.DateField()),
                ('resolved', models.BooleanField(default=False)),
            ],
        ),
    ]
