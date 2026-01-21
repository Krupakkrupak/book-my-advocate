from rest_framework import serializers
from .models import Advocate, Case

class AdvocateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Advocate
        fields = '__all__'

class CaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Case
        fields = '__all__'

class AdvocateSuccessRateSerializer(serializers.Serializer):
    advocate_id = serializers.IntegerField()
    advocate_name = serializers.CharField()
    total_closed_cases = serializers.IntegerField()
    won_cases = serializers.IntegerField()
    success_rate = serializers.FloatField()
