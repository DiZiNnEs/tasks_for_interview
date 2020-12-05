from rest_framework import serializers


class ScoreSerializer(serializers.Serializer):
    first_json = serializers.JSONField()
    second_json = serializers.JSONField()
