# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import geoposition.fields


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20151214_2107'),
    ]

    operations = [
        migrations.AddField(
            model_name='locations',
            name='position',
            field=geoposition.fields.GeopositionField(max_length=42, null=True, blank=True),
            preserve_default=True,
        ),
    ]
