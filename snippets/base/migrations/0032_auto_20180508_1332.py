# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-05-08 13:32
from __future__ import unicode_literals

from django.db import migrations

from django_mysql.models.functions import AsType, ColumnAdd


def migrate_has_testpilot(apps, schema_editor):
    Snippet = apps.get_model('base', 'Snippet')
    Snippet.objects.filter(client_options__has_testpilot_CHAR='yes').update(
        client_options=ColumnAdd(
            'client_options', {
                'addon_check_type': AsType('installed', 'CHAR'),
                'addon_name': AsType('@testpilot-addon', 'CHAR'),
            })
    )
    Snippet.objects.filter(client_options__has_testpilot_CHAR='not').update(
        client_options=ColumnAdd(
            'client_options', {
                'addon_check_type': AsType('not_installed', 'CHAR'),
                'addon_name': AsType('@testpilot-addon', 'CHAR'),
            })
    )
    Snippet.objects.filter(client_options__has_testpilot_CHAR='any').update(
        client_options=ColumnAdd(
            'client_options', {
                'addon_check_type': AsType('any', 'CHAR'),
                'addon_name': AsType('', 'CHAR'),
            })
    )


def noop(apps, schema_editor):
    # nothing needed to go back in time.
    pass


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0031_auto_20180515_0733'),
    ]

    operations = [
        migrations.RunPython(migrate_has_testpilot, noop),
    ]