# Generated by Django 2.1.15 on 2023-07-24 01:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_auto_20230723_1828'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='activaciones',
            name='id',
        ),
        migrations.AlterField(
            model_name='activaciones',
            name='documento',
            field=models.FloatField(primary_key=True, serialize=False),
        ),
    ]
