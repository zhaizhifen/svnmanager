# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-05-24 04:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='cron_info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cron_name', models.CharField(max_length=100, verbose_name='\u4efb\u52a1\u540d')),
                ('cron_status', models.CharField(choices=[('stop', '\u7981\u7528'), ('run', '\u542f\u7528')], default='stop', max_length=32, verbose_name='\u72b6\u6001')),
                ('cron_rule', models.CharField(max_length=50, verbose_name='\u65f6\u95f4\u89c4\u5219')),
                ('cron_cmd', models.CharField(max_length=512, verbose_name='\u547d\u4ee4')),
                ('cron_service_ip', models.GenericIPAddressField(verbose_name='\u8fd0\u884c\u7684\u670d\u52a1\u5668IP')),
                ('crom_memo', models.CharField(blank=True, max_length=200, null=True, verbose_name='\u529f\u80fd\u5907\u6ce8')),
                ('cron_owner', models.CharField(max_length=150, verbose_name='\u521b\u5efa\u4eba')),
            ],
            options={
                'verbose_name': '\u4efb\u52a1\u7ba1\u7406',
                'verbose_name_plural': '\u4efb\u52a1\u7ba1\u7406',
            },
        ),
    ]
