from rest_framework import serializers
from . import models

class SlidesSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Slides
        fields = ('name','image',)
