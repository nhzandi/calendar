# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('instrument', '0002_numofmonth_numberofdays'),
    ]

    operations = [
        migrations.AlterField(
            model_name='numofday',
            name='number',
            field=models.IntegerField(default=1, unique=True),
        ),
        migrations.AlterField(
            model_name='numofmonth',
            name='number',
            field=models.IntegerField(default=0, unique=True),
        ),
        migrations.AlterField(
            model_name='numofyear',
            name='number',
            field=models.IntegerField(default=2000, unique=True),
        ),
    ]
