from rest_framework import serializers
from .models import Movie, Director

class MovieSerializer(serializers.ModelSerializer):
    director_name = serializers.ReadOnlyField(source='director.name')

    class Meta:
        model = Movie
        fields = [
            'id', 'title', 'genre', 'director', 'director_name', 
            'release_year', 'synopsis', 'duration_minutes', 
            'rating', 'created_at', 'updated_at'
        ]
        read_only_fields = ['created_at', 'updated_at']

    def get_movies_count(self, obj):
        return obj.movies.count()
    
class DirectorDetailSerializer(DirectorSerializer):
    """
    Serializer detallado para Director
    Incluye la lista completa de sus películas
    """
    movies = MovieSerializer(many=True, read_only=True)
    
    class Meta(DirectorSerializer.Meta):
        fields = DirectorSerializer.Meta.fields + ['movies']