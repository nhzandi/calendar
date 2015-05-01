# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('instrument', '0006_userprofile'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='website',
            field=models.URLField(default=b'http://www.a.com', blank=True),
            preserve_default=True,
        ),
    ]
