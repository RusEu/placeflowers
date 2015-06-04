# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('thumbnails', '0002_auto_20150603_1217'),
    ]

    operations = [
        migrations.AddField(
            model_name='flower',
            name='image_type',
            field=models.TextField(default=b'square', max_length=30),
        ),
        migrations.AlterField(
            model_name='flower',
            name='image',
            field=models.ImageField(null=True, upload_to=b'static/flowers', blank=True),
        ),
    ]
