# Generated by Django 2.2.6 on 2019-10-21 11:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0019_target_filtr_operating_system'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='limit_blocks',
            field=models.PositiveIntegerField(blank=True, default=0, help_text='Job will complete if number of Blocks exceeds this number. Set to 0 to disable.', verbose_name='Global Block Limit'),
        ),
        migrations.AddField(
            model_name='job',
            name='limit_clicks',
            field=models.PositiveIntegerField(blank=True, default=0, help_text='Job will complete if number of Clicks exceeds this number. Set to 0 to disable.', verbose_name='Global Clicks Limit'),
        ),
        migrations.AddField(
            model_name='job',
            name='limit_impressions',
            field=models.PositiveIntegerField(blank=True, default=0, help_text='Job will complete if number of Impressions exceeds this number. Set to 0 to disable.', verbose_name='Global Impressions Limit'),
        ),
    ]