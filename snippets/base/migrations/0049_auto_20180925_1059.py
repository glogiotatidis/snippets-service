# Generated by Django 2.1.1 on 2018-09-25 10:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0048_auto_20180919_0816'),
    ]

    operations = [
        migrations.AddField(
            model_name='asrsnippet',
            name='weight',
            field=models.IntegerField(choices=[(33, 'Appear 1/3rd as often as an average snippet'), (50, 'Appear half as often as an average snippet'), (66, 'Appear 2/3rds as often as an average snippet'), (100, 'Appear as often as an average snippet'), (150, 'Appear 1.5 times as often as an average snippet'), (200, 'Appear twice as often as an average snippet'), (300, 'Appear three times as often as an average snippet')], default=100, help_text='How often should this snippet be shown to users?', verbose_name='Prevalence'),
        ),
    ]
