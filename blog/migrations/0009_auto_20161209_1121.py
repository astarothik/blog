# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_auto_20161209_1100'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='text',
            field=ckeditor.fields.RichTextField(),
        ),
        migrations.AlterField(
            model_name='post',
            name='text_new',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
