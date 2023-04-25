from rest_framework import serializers
from doctor.models import doctor

class doctorserializer(serializers.ModelSerializer):
    class Meta:
        model=doctor
        fields="__all__"