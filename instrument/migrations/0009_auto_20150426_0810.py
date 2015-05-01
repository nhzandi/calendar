# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('instrument', '0008_auto_20150426_0808'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='website',
            field=models.URLField(default=b'http://', blank=True),
        ),
    ]
