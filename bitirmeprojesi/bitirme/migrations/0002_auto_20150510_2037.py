# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bitirme', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='kampanya',
            old_name='aktif',
            new_name='onay',
        ),
    ]
