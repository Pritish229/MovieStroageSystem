# Generated by Django 4.0.4 on 2022-05-24 02:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App_Flow', '0003_product_detils_alter_cardata_car_desc_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product_detils',
            name='Product_Description',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]
