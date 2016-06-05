# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0004_auto_20160430_1759'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='article_anot',
            field=models.CharField(default=b'', max_length=100),
        ),
    ]
