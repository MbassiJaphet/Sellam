# Generated by Django 2.2.3 on 2019-07-17 01:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_product_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(default='default.png', upload_to='products'),
            preserve_default=False,
        ),
    ]
