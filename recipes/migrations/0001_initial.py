# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=100)),
                ('instructions', models.TextField()),
                ('tag', models.CharField(max_length=20, null=True, blank=True)),
                ('image', models.ImageField(null=True, upload_to=b'images', blank=True)),
                ('views', models.IntegerField(default=0)),
            ],
        ),
    ]
