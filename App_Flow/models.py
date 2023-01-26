
from distutils.command.upload import upload
from django.db import models


# Create your models here.


class moviedata(models.Model):
    movie_name = models.CharField(max_length=30, null= True)
    movie_id = models.CharField(max_length=30, null= True)
    movie_rating = models.CharField(max_length=30, null= True)
    movie_image = models.ImageField(upload_to = 'imgs/')
    movie_description = models.TextField()

    def __str__(self) -> str:
        return self.movie_name

