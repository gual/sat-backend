from rest_framework import serializers
from taxes.models import Token, Determinant, TaxableIncome, Rate, RateRange, DeclarationPaymentMode, Tax


class TokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Token
        fields = '__all__'


class DeterminantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Determinant
        fields = '__all__'


class TaxableIncomeSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaxableIncome
        fields = '__all__'


class RateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rate
        fields = '__all__'


class RateRangeSerializer(serializers.ModelSerializer):
    class Meta:
        model = RateRange
        fields = '__all__'


class DeclarationPaymentModeSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeclarationPaymentMode
        fields = '__all__'


class TaxSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tax
        fields = '__all__'
