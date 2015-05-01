# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('instrument', '0003_auto_20150421_1642'),
    ]

    operations = [
        migrations.AlterField(
            model_name='numofday',
            name='number',
            field=models.IntegerField(default=1),
        ),
    ]
