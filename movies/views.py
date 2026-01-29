from rest_frmaework import viewsets, filters, status
from rest_framework import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend

from .models import Movie, Director
from .serializers import (
    Movieserializer,
    DirectorSerializer,
    DirectorDetailSerializer
)

class DirectorViewSet(viewsets.ModelViewSet):
    queryset = Director.objects.all()
    serializer_class = DirectorSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name', 'nationality']
    ordering_fields = ['name', 'created_at']
    ordering = ['name']

def get_serializer_class(self):
        if self.action == 'retrieve':
            return DirectorDetailSerializer
        return DirectorSerializer

@action(detail=True, methods=['get'])
def movies(self, request, pk=None):
    director = self.get_object()
    movies = director.movies.all()
    serializer = MovieSerializer(movies, many=True)
    return Response(serializer.data)





