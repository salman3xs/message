from dataclasses import field
from statistics import mode
from rest_framework import serializers
from . import models

class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Message
        fields = ['message']