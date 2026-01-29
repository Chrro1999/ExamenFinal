# movies/models.py
from django.db import models

# Modelos para la aplicación de películas */
class Director(models.Model): 
    name = models.CharField(max_length=150)
    nationality = models.CharField(max_length=100, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    biography = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Meta:
        ordering = ['name']
        verbose_name = "Director"
        verbose_name_plural = "Directores"

def __str__(self):
        return self.name

#Modelos para la aplicacion de peliculas

class Movie(models.Model):
    title = models.CharField(max_length=200)
    genre = models.CharField(max_length=100)
    director = models.ForeignKey(
        Director, 
        on_delete=models.CASCADE, 
        related_name='movies' #Permite acceder a las peliculas desde el director
    )
    release_year = models.PositiveIntegerField()  
    synopsis = models.TextField()
    duration_minutes = models.DateTimeField(auto_now_add=True)
    rating = models.DecimalField(max_digits=3, decimal_places=1, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-release_year', 'title']
        verbose_name = "Movie"
        verbose_name_plural = "Movies"

    def __str__(self):
        return f"{self.title} ({self.release_year})"