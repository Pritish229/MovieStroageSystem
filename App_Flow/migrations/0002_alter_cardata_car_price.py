# Generated by Django 4.0.4 on 2022-05-18 06:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App_Flow', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cardata',
            name='Car_Price',
            field=models.IntegerField(),
        ),
    ]
