# Generated by Django 3.1.1 on 2021-01-29 11:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('engine', '0036_auto_20201216_0943'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='subset',
            field=models.CharField(blank=True, default='', max_length=64),
        ),
    ]