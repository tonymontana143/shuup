# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-09-02 09:08
from __future__ import unicode_literals

import django.db.models.deletion
import enumfields.fields
import jsonfield.fields
from django.conf import settings
from django.db import migrations, models

import shuup.utils.analog


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('shuup_notify', '0006_shop_not_null'),
    ]

    operations = [
        migrations.CreateModel(
            name='ScriptLogEntry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now_add=True, verbose_name='created on')),
                ('message', models.CharField(max_length=256, verbose_name='message')),
                ('identifier', models.CharField(blank=True, max_length=64, verbose_name='identifier')),
                ('kind', enumfields.fields.EnumIntegerField(default=0, enum=shuup.utils.analog.LogEntryKind, verbose_name='log entry kind')),
                ('extra', jsonfield.fields.JSONField(blank=True, null=True, verbose_name='extra data')),
                ('target', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='log_entries', to='shuup_notify.Script', verbose_name='target')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='user')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
