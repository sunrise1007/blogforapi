from rest_framework import serializers
from .models import Singer, Song, CarModel, FuelType, Car, Ceo


class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = ['id', 'title', 'singer', 'duration']


class SingerSerializer(serializers.ModelSerializer):
    song = serializers.HyperlinkedIdentityField(view_name='song-detail')

    class Meta:
        model = Singer
        fields = ['id', 'name', 'gender', 'song']

        '''Add song field that has been defined in models.py in ForeignKey
                relationship. It will show song associated with the singers'''


class CarModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarModel
        fields = ['id', 'name', 'fueltype']


class FuelTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = FuelType
        fields = ['id', 'name']


class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = ['id', 'name']


class CeoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ceo
        fields = ['id', 'car', 'name']
