# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Kampanya',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('olusturulma', models.DateTimeField(auto_now_add=True)),
                ('baslik', models.CharField(default=b'', max_length=100, blank=True)),
                ('icerik', models.TextField()),
                ('aktif', models.BooleanField(default=False)),
            ],
            options={
                'ordering': ('olusturulma',),
            },
        ),
    ]
