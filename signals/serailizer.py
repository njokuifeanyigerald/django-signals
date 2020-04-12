from rest_framework import serializers
from .models import Signal

class SignalSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Signal
        fields = ('id','url','name', 'age','complexion', 'job',)
        
    