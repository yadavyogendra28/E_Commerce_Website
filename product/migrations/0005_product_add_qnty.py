# Generated by Django 4.1.3 on 2023-04-22 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0004_product_electronics_product_fashion_product_home_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product_add',
            name='qnty',
            field=models.CharField(default=1, max_length=5),
            preserve_default=False,
        ),
    ]
