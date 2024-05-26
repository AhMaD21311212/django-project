# Generated by Django 3.2.23 on 2024-01-09 09:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_auto_20240107_1033'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='color',
            field=models.ManyToManyField(related_name='products', to='product.Color'),
        ),
        migrations.AlterField(
            model_name='product',
            name='size',
            field=models.ManyToManyField(related_name='products', to='product.Size'),
        ),
    ]