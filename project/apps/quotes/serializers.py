from rest_framework import serializers
from . import models

class QuotesSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Quotes
        fields = ('numbercopies','numbersets','sheetsizes','sheettypes',
        'extras','file','name','email','phone','enterprise','city','branch')
