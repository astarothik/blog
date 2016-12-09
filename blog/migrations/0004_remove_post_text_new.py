# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_post_text_new'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='text_new',
        ),
    ]
