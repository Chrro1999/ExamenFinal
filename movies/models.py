# movies/models.py
from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=200)
    genre = models.CharField(max_length=100)
    director = models.CharField(max_length=150)
    release_year = models.PositiveIntegerField()  
    synopsis = models.TextField()

    def __str__(self):
        return f"{self.title} ({self.release_year})"