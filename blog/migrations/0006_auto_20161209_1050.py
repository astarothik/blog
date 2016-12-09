# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_post_text_new'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='text',
            field=ckeditor.fields.RichTextField(blank=True, default=''),
        ),
    ]
