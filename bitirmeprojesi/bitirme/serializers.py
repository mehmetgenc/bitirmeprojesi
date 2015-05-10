__author__ = 'mehmetgenc'

from django.forms import widgets
from rest_framework import serializers
from bitirme.models import Kampanya

class KampanyaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Kampanya
        fields = ('id', 'baslik', 'icerik', 'onay')

