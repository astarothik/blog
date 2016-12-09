# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import ckeditor.widgets


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_pagesettings'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='text',
            field=models.TextField(verbose_name=ckeditor.widgets.CKEditorWidget),
        ),
    ]
