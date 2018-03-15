from rest_framework import serializers
from .models import Shoe


class ShoeSerializer(serializers.ModelSerializer):

    class Meta:

        model = Shoe
        fields = ('name', 'price')
        # fields = '__all__' serializes all the fields instead of specific ones
