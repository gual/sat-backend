from rest_framework import serializers
from taxes.models import Token, Determinant, TaxableIncome, Rate, RateRange, DeclarationPaymentMode, Tax
import logging

logger = logging.getLogger(__name__)


class TokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Token
        fields = '__all__'


class DeterminantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Determinant
        fields = '__all__'


class TaxableIncomeSerializer(serializers.ModelSerializer):
    tokens = TokenSerializer(many=True)

    class Meta:
        model = TaxableIncome
        fields = '__all__'
        depth = 2

    def create(self, validated_data):
        tokens_data = validated_data.pop('tokens')
        taxable_income = TaxableIncome.objects.create(**validated_data)

        for token_data in tokens_data:
            token = Token.objects.create(**token_data)
            taxable_income.tokens.add(token)

        return taxable_income


class RateRangeSerializer(serializers.ModelSerializer):
    class Meta:
        model = RateRange
        fields = '__all__'


class RateSerializer(serializers.ModelSerializer):
    tokens = TokenSerializer(many=True)
    determinants = DeterminantSerializer(many=True)
    ranges = RateRangeSerializer(many=True)

    class Meta:
        model = Rate
        fields = '__all__'
        depth = 2

    def create(self, validated_data):
        tokens_data = validated_data.pop('tokens')
        determinants_data = validated_data.pop('determinants')
        ranges_data = validated_data.pop('ranges')
        rate = Rate.objects.create(**validated_data)

        for token_data in tokens_data:
            token = Token.objects.create(**token_data)
            rate.tokens.add(token)

        for determinant_data in determinants_data:
            determinant = Determinant.objects.create(**determinant_data)
            rate.determinants.add(determinant)

        for range_data in ranges_data:
            rate_range = RateRange.objects.create(**range_data)
            rate.ranges.add(rate_range)

        return rate


class DeclarationPaymentModeSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeclarationPaymentMode
        fields = '__all__'


class TaxSerializer(serializers.ModelSerializer):
    taxable_income_id = serializers.IntegerField()
    rate_id = serializers.IntegerField()
    declaration_payment_mode = DeclarationPaymentModeSerializer
    determinants = DeterminantSerializer(many=True)

    class Meta:
        model = Tax
        fields = '__all__'
        depth = 4
        extra_kwargs = {
            "declaration_payment_mode": {"read_only": False},
            "determinants": {"read_only": False}
        }

    def create(self, validated_data):
        declaration_payment_mode_data = validated_data.pop('declaration_payment_mode')
        determinants_data = validated_data.pop('determinants')

        taxable_income = TaxableIncome.objects.get(pk=validated_data['taxable_income_id'])
        rate = Rate.objects.get(pk=validated_data['rate_id'])
        declaration_payment_mode = DeclarationPaymentMode.objects.create(**declaration_payment_mode_data)

        tax = Tax.objects.create(
            declaration_payment_mode=declaration_payment_mode,
            taxable_income=taxable_income,
            rate=rate,
            **validated_data
        )

        for determinant_data in determinants_data:
            determinant = Determinant.objects.create(**determinant_data)
            tax.determinants.add(determinant)

        return tax
