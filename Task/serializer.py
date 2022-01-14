from itertools import product
from rest_framework import serializers
from .models import RandomUUID


class RandomUUIDSerializers(serializers.ModelSerializer):
    class Meta:
        model = RandomUUID
        fields = ("key", "value")