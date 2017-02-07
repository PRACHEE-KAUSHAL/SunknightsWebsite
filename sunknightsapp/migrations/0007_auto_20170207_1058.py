# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-02-07 10:58
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('sunknightsapp', '0006_auto_20170206_0009'),
    ]

    operations = [
        migrations.RenameField(
            model_name='dailyquest',
            old_name='task',
            new_name='questtext',
        ),
        migrations.AddField(
            model_name='dailyquest',
            name='permed',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='dailyquest',
            name='tier',
            field=models.PositiveSmallIntegerField(choices=[(1, 'Tier 1'), (2, 'Tier 2'), (3, 'Tier 3')], default=1),
        ),
        migrations.AddField(
            model_name='pointsinfo',
            name='permquestcd',
            field=models.DateTimeField(auto_now_add=True, db_index=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
