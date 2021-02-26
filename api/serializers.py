from rest_framework import serializers
from .serializers import *
from .models import Piza, Size, Toping
class PizaSeriaizer(serializers.ModelSerializer):
    class Meta:
        model=Piza
        fields='__all__'
    

class SizeSeriaizer(serializers.ModelSerializer):
    class Meta:
        model=Size
        fields='__all__'

class TopingSeriaizer(serializers.ModelSerializer):
    class Meta:
        model=Toping
        fields='__all__'

