# Generated by Django 4.1.3 on 2023-04-22 12:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0005_product_add_qnty'),
    ]

    operations = [
        migrations.AddField(
            model_name='product_electronics',
            name='qnty',
            field=models.CharField(default=5, max_length=5),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product_fashion',
            name='qnty',
            field=models.CharField(default=5, max_length=5),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product_grocery',
            name='qnty',
            field=models.CharField(default=5, max_length=5),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product_home',
            name='qnty',
            field=models.CharField(default=5, max_length=5),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product_mobiles',
            name='qnty',
            field=models.CharField(default=5, max_length=5),
            preserve_default=False,
        ),
    ]