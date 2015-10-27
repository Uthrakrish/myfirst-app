# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kissflow', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='kissflow',
            name='text',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]
