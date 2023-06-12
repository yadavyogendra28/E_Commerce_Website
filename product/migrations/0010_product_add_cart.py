# Generated by Django 4.1.3 on 2023-05-13 23:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0009_rating'),
    ]

    operations = [
        migrations.CreateModel(
            name='product_Add_Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=50)),
                ('img', models.ImageField(upload_to='Media')),
                ('title', models.CharField(max_length=50)),
                ('Quantity', models.IntegerField()),
                ('Price', models.IntegerField()),
                ('about_p', models.TextField()),
            ],
        ),
    ]