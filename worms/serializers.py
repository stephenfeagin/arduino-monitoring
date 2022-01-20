from rest_framework import serializers
from worms.models import Measurement


class MeasurementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Measurement
        fields = ["id", "insert_timestamp", "humidity", "temperature"]