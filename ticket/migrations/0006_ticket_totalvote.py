# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ticket', '0005_auto_20180102_1800'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='totalvote',
            field=models.IntegerField(default=0),
        ),
    ]
