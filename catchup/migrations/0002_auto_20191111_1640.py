# Generated by Django 2.2.7 on 2019-11-11 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catchup', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventphoto',
            name='description',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]