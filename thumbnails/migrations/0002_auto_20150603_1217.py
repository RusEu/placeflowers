# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('thumbnails', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flower',
            name='image',
            field=models.ImageField(null=True, upload_to=b'/static/flowers', blank=True),
        ),
    ]
