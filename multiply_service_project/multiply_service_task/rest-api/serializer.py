from rest_framework import serializers


class ScoreSerializer(serializers.Serializer):
    multipliers = serializers.ListField(child=serializers.IntegerField())
