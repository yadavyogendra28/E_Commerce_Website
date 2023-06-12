# Generated by Django 4.1.3 on 2023-04-21 20:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_product_add'),
    ]

    operations = [
        migrations.CreateModel(
            name='product_Grocery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='Media')),
                ('title', models.CharField(max_length=50)),
                ('about_p', models.TextField()),
            ],
        ),
        migrations.AlterField(
            model_name='product_add',
            name='about_p',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='product_add',
            name='img',
            field=models.ImageField(upload_to='Media'),
        ),
    ]