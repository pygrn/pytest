# Generated by Django 2.2.7 on 2019-11-13 19:18

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catchup', '0002_auto_20191111_1640'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='event_date',
        ),
        migrations.RemoveField(
            model_name='event',
            name='event_time',
        ),
        migrations.AddField(
            model_name='event',
            name='event_datetime',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='max_attendees',
            field=models.IntegerField(default=0, help_text='0 = unlimited', validators=[django.core.validators.MinValueValidator(0)]),
        ),
    ]
