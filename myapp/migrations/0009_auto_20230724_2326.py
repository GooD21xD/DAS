# Generated by Django 2.1.15 on 2023-07-25 04:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0008_auto_20230724_2324'),
    ]

    operations = [
        migrations.AlterField(
            model_name='facturacion',
            name='fec_facturacion',
            field=models.DateField(null=True),
        ),
    ]