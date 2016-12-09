# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20161209_1050'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='text',
            field=models.TextField(),
        ),
    ]
