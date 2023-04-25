from rest_framework import serializers
from appointment.models import parchi

class parchiserializer(serializers.ModelSerializer):
    class Meta:
        model=parchi
        fields="__all__"