from rest_framework import viewsets
from taxes.models import Token, Determinant, TaxableIncome, Rate, RateRange, DeclarationPaymentMode, Tax
from taxes.serializers import TokenSerializer, DeterminantSerializer, TaxableIncomeSerializer, RateSerializer, \
    RateRangeSerializer, DeclarationPaymentModeSerializer, TaxSerializer


class TokenViewSet(viewsets.ModelViewSet):
    queryset = Token.objects.all()
    serializer_class = TokenSerializer


class DeterminantViewSet(viewsets.ModelViewSet):
    queryset = Determinant.objects.all()
    serializer_class = DeterminantSerializer


class TaxableIncomeViewSet(viewsets.ModelViewSet):
    queryset = TaxableIncome.objects.all()
    serializer_class = TaxableIncomeSerializer


class RateViewSet(viewsets.ModelViewSet):
    queryset = Rate.objects.all()
    serializer_class = RateSerializer


class RateRangeViewSet(viewsets.ModelViewSet):
    queryset = RateRange.objects.all()
    serializer_class = RateRangeSerializer


class DeclarationPaymentModeViewSet(viewsets.ModelViewSet):
    queryset = DeclarationPaymentMode.objects.all()
    serializer_class = DeclarationPaymentModeSerializer


class TaxViewSet(viewsets.ModelViewSet):
    queryset = Tax.objects.all()
    serializer_class = TaxSerializer
