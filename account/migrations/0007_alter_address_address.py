# Generated by Django 3.2.23 on 2024-01-05 07:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0006_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='address',
            field=models.CharField(max_length=500),
        ),
    ]