# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('instrument', '0004_auto_20150421_1704'),
    ]

    operations = [
        migrations.AlterField(
            model_name='numofmonth',
            name='name',
            field=models.CharField(max_length=15),
        ),
        migrations.AlterField(
            model_name='numofmonth',
            name='number',
            field=models.IntegerField(default=0),
        ),
    ]
