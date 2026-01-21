from rest_framework import serializers
from .models import Advocate, Case

class AdvocateSerializer(serializers.ModelSerializer):
    user = serializers.StringField(read_only=True)
    specialization = serializers.CharField(max_length=100)
    experience_years = serializers.IntegerField()
    education = serializers.CharField()
    bio = serializers.CharField()
    hourly_rate = serializers.DecimalField(max_digits=10, decimal_places=2)
    availability = serializers.BooleanField()
    created_at = serializers.DateTimeField(read_only=True)
    
    class Meta:
        model = Advocate
        fields = '__all__'


class CaseSerializer(serializers.ModelSerializer):
    client = serializers.StringField(read_only=True)
    advocate = AdvocateSerializer(read_only=True)
    title = serializers.CharField(max_length=200)
    description = serializers.CharField()
    case_type = serializers.CharField(max_length=100)
    status = serializers.CharField()
    created_at = serializers.DateTimeField(read_only=True)
    updated_at = serializers.DateTimeField(read_only=True)
    closed_at = serializers.DateTimeField(read_only=True)
    
    class Meta:
        model = Case
        fields = '__all__'


class SuccessRateSerializer(serializers.Serializer):
    success_rate = serializers.FloatField()
    total_closed_cases = serializers.IntegerField()
    won_cases = serializers.IntegerField()
    lost_cases = serializers.IntegerField()
    calculation_details = serializers.DictField()
