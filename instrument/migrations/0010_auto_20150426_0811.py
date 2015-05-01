# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('instrument', '0009_auto_20150426_0810'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='website',
            field=models.URLField(default=None, blank=True),
        ),
    ]
