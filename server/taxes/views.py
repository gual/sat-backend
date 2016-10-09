from rest_framework import viewsets
from taxes.models import Law, Tax, Calculation
from taxes.serializers import LawSerializer, TaxSerializer,CalculationSerializer


class LawViewSet(viewsets.ModelViewSet):
    """ ViewSet for viewing and editing Law objects """
    queryset = Law.objects.all()
    serializer_class = LawSerializer


class TaxViewSet(viewsets.ModelViewSet):
    """ ViewSet for viewing and editing Tax objects """
    queryset = Tax.objects.all()
    serializer_class = TaxSerializer


class CalculationViewSet(viewsets.ModelViewSet):
    """ ViewSet for viewing and editing Calculation objects """
    queryset = Calculation.objects.all()
    serializer_class = CalculationSerializer