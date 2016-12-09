# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_auto_20161209_1147'),
    ]

    operations = [
        migrations.CreateModel(
            name='PageSettings',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name_website', models.TextField(verbose_name='Название сайта', max_length=20)),
                ('descriptor_website', models.TextField(verbose_name='Описание сайта', max_length=50)),
            ],
        ),
    ]
