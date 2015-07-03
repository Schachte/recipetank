# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20150703_1131'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='content',
            new_name='instructions',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='title',
            new_name='name',
        ),
    ]
