# Generated by Django 3.2.23 on 2024-01-09 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0005_auto_20240109_1248'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='slug',
            field=models.SlugField(default=1),
            preserve_default=False,
        ),
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