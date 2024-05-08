from django.db import models


class Singer(models.Model):
    name = models.CharField(max_length=100)
    gender = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Song(models.Model):
    title = models.CharField(max_length=100)
    singer = models.ForeignKey(Singer, on_delete=models.CASCADE,
                               related_name='song')
    duration = models.IntegerField()

    def __str__(self):
        return self.title


class FuelType(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class CarModel(models.Model):
    name = models.CharField(max_length=255)
    fueltype = models.ManyToManyField(FuelType)

    def __str__(self):
        return self.name


class Car(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Ceo(models.Model):
    car = models.OneToOneField(Car, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.name
