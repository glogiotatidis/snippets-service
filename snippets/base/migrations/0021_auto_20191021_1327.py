# Generated by Django 2.2.6 on 2019-10-21 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0020_auto_20191021_1115'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='client_limit_lifetime',
            field=models.PositiveIntegerField(default=0, verbose_name='Max Lifetime Impressions'),
        ),
        migrations.AddField(
            model_name='job',
            name='client_limit_per_day',
            field=models.PositiveIntegerField(default=0, verbose_name='Max Daily Impressions'),
        ),
        migrations.AddField(
            model_name='job',
            name='client_limit_per_fortnight',
            field=models.PositiveIntegerField(default=0, verbose_name='Max Fortnightly Impressions'),
        ),
        migrations.AddField(
            model_name='job',
            name='client_limit_per_hour',
            field=models.PositiveIntegerField(default=0, verbose_name='Max Hourly Impressions'),
        ),
        migrations.AddField(
            model_name='job',
            name='client_limit_per_month',
            field=models.PositiveIntegerField(default=0, verbose_name='Max Monthly Impressions'),
        ),
        migrations.AddField(
            model_name='job',
            name='client_limit_per_week',
            field=models.PositiveIntegerField(default=0, verbose_name='Max Weekly Impressions'),
        ),
    ]
