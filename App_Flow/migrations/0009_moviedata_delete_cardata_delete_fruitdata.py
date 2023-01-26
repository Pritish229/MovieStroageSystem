# Generated by Django 4.1.5 on 2023-01-26 11:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("App_Flow", "0008_fruitdata_fruit_image"),
    ]

    operations = [
        migrations.CreateModel(
            name="moviedata",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("movie_name", models.CharField(max_length=30, null=True)),
                ("movie_id", models.CharField(max_length=30, null=True)),
                ("movie_Price", models.CharField(max_length=30, null=True)),
                ("movie_image", models.ImageField(upload_to="imgs/")),
                ("movie_description", models.TextField()),
            ],
        ),
        migrations.DeleteModel(name="CarData",),
        migrations.DeleteModel(name="fruitdata",),
    ]