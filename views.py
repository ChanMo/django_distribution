import json

from django.shortcuts import render
from django.views.generic.detail import DetailView
from rest_framework.generics import RetrieveAPIView
from rest_framework.mixins import RetrieveModelMixin

from .models import *
from .serializers import *


class AppApiView(RetrieveAPIView):
    queryset = App.objects.all()
    serializer_class = AppSerializer
    lookup_field = 'slug'


class AppView(DetailView):
    model = App
    lookup_field = 'slug'
    template_name = 'distribution/index.html'
