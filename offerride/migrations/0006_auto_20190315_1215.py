# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2019-03-15 12:15
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('offerride', '0005_auto_20190314_0933'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Driver',
        ),
        migrations.RenameField(
            model_name='ride',
            old_name='driverid',
            new_name='username',
        ),
    ]
