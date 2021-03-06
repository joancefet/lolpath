# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-14 20:51
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('lolpath', '0003_auto_20170614_1240'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='summoner',
            name='summoner_id',
        ),
        migrations.AddField(
            model_name='summoner',
            name='lolpath_user_id',
            field=models.ForeignKey(default=False, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='summoner',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
