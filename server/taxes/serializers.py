from rest_framework import serializers
from taxes.models import Law, Tax, Calculation

class LawSerializer(serializers.ModelSerializer):
    """Serializer to represent the Law model"""
    class Meta:
        model = Law
        fields = ("name")

class TaxSerializer(serializers.ModelSerializer):
    """Serializer to represent the Tax model"""
    class Meta:
        model = Tax
        fields = ("law", "name")

class CalculationSerializer(serializers.ModelSerializer):
    """Serializer to represent the Calculation model"""
    class Meta:
        model = Calculation
        field = ("tax", "taxable", "surplus", "value", "description")