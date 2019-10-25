from rest_framework import serializers
from . import models

class ServicesSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Services
        fields = ('name','description','sheetsizes','sheettypes','extras','image')

class SheetSizesSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.SheetSizes
        fields = ('description',)

class SheetTypesSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.SheetTypes
        fields = ('description',)

class ExtrasSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Extras
        fields = ('description',)
