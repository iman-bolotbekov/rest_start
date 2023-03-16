from django.shortcuts import render
from rest_framework import viewsets, mixins

from . import models
from . import serializers


class AuthorViewSet(viewsets.mixins.CreateModelMixin, viewsets.GenericViewSet):
    queryset = models.Author.objects.all()
    serializer_class = serializers.AuthorSerializer





