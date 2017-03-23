from rest_framework import serializers
from katas.models import Kata

class KataSerializer(serializers.ModelSerializer):
    class Meta:
        model =Kata
        fields = ('id', 'name', 'description', 'created')