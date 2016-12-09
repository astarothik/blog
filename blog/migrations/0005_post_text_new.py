# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_remove_post_text_new'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='text_new',
            field=ckeditor.fields.RichTextField(default='', blank=True),
        ),
    ]
