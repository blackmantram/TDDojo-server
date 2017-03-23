from django.shortcuts import render

from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from katas.models import Kata
from katas.serializers import KataSerializer
from rest_framework import generics


class KataList(generics.ListCreateAPIView):
    queryset = Kata.objects.all()
    serializer_class = KataSerializer


class KataDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Kata.objects.all()
    serializer_class = KataSerializer