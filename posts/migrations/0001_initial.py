# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Posts',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('lab_name', models.CharField(default=b'', max_length=30)),
                ('browser', models.BooleanField(default=False)),
                ('resume', models.BooleanField(default=False)),
                ('job', models.BooleanField(default=False)),
                ('video', models.BooleanField(default=False)),
                ('game', models.BooleanField(default=False)),
                ('email', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
