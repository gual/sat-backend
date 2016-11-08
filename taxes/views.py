from rest_framework import viewsets
from taxes.models import TaxableIncome, Rate,  Tax
from taxes.serializers import TaxableIncomeSerializer, RateSerializer, TaxSerializer


class TaxableIncomeViewSet(viewsets.ModelViewSet):
    queryset = TaxableIncome.objects.all()
    serializer_class = TaxableIncomeSerializer


class RateViewSet(viewsets.ModelViewSet):
    queryset = Rate.objects.all()
    serializer_class = RateSerializer


class TaxViewSet(viewsets.ModelViewSet):
    queryset = Tax.objects.all()
    serializer_class = TaxSerializer
