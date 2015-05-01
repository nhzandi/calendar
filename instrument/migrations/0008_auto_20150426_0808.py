# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('instrument', '0007_userprofile_website'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='website',
            field=models.URLField(default=b'', blank=True),
        ),
    ]
