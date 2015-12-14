# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_review'),
    ]

    operations = [
        migrations.AddField(
            model_name='locations',
            name='alcohol',
            field=models.IntegerField(blank=True, null=True, choices=[(0, 'no'), (1, 'yes')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='review',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime.now),
            preserve_default=True,
        ),
    ]
