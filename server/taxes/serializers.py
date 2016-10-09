from rest_framework import serializers
from taxes.models import Law, Tax, Calculation

class LawSerializer(serializers.ModelSerializer):
    """Serializer to represent the Law model"""
    class Meta:
        model = Law
        fields = '__all__'

class TaxSerializer(serializers.ModelSerializer):
    """Serializer to represent the Tax model"""
    class Meta:
        model = Tax
        fields = '__all__'

class CalculationSerializer(serializers.ModelSerializer):
    """Serializer to represent the Calculation model"""
    class Meta:
        model = Calculation
        field = '__all__'