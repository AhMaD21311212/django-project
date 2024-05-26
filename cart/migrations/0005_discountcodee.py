# Generated by Django 3.2.23 on 2024-01-06 07:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0004_order_total_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='DiscountCodee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('discount', models.SmallIntegerField(default=0)),
                ('quantity', models.PositiveIntegerField(default=0)),
            ],
        ),
    ]
