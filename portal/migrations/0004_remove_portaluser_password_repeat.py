# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0003_auto_20151103_2011'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='portaluser',
            name='password_repeat',
        ),
    ]
