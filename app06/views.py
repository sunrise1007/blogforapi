from rest_framework import viewsets
from .models import Singer, Song, CarModel, FuelType, Car, Ceo
from .serializers import SingerSerializer, SongSerializer, CarSerializer, FuelTypeSerializer, CeoSerializer, CarModelSerializer


class SingerViewSet(viewsets.ModelViewSet):
    queryset = Singer.objects.all()
    serializer_class = SingerSerializer


class SongViewSet(viewsets.ModelViewSet):
    queryset = Song.objects.all()
    serializer_class = SongSerializer


class CarModelViewSet(viewsets.ModelViewSet):
    queryset = CarModel.objects.all()
    serializer_class = CarModelSerializer


class FuelTypeViewSet(viewsets.ModelViewSet):
    queryset = FuelType.objects.all()
    serializer_class = FuelTypeSerializer


class CarViewSet(viewsets.ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializer


class CeoViewSet(viewsets.ModelViewSet):
    queryset = Ceo.objects.all()
    serializer_class = CeoSerializer
