# Generated by Django 4.0.4 on 2022-06-04 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App_Flow', '0006_delete_product_detil'),
    ]

    operations = [
        migrations.CreateModel(
            name='fruitdata',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Fruit_name', models.CharField(max_length=30, null=True)),
                ('Fruit_id', models.CharField(max_length=30, null=True)),
                ('Fruit_Price', models.CharField(max_length=30, null=True)),
                ('Fruit_description', models.CharField(max_length=30, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='cardata',
            name='Car_Image',
            field=models.ImageField(upload_to='imgs/'),
        ),
    ]
