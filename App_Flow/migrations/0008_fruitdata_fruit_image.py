# Generated by Django 4.0.4 on 2022-06-04 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App_Flow', '0007_fruitdata_alter_cardata_car_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='fruitdata',
            name='Fruit_image',
            field=models.ImageField(default=1, upload_to='imgs/'),
            preserve_default=False,
        ),
    ]
