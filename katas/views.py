from katas.models import Kata
from katas.serializers import KataSerializer
from rest_framework import generics


class KataList(generics.ListCreateAPIView):
    queryset = Kata.objects.all()
    serializer_class = KataSerializer


class KataDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Kata.objects.all()
    serializer_class = KataSerializer