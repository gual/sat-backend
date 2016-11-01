from rest_framework import viewsets

from contributors.models import Establishment, Property
from contributors.serializers import EstablishmentSerializer, PropertySerializer


class EstablishmentViewSet(viewsets.ModelViewSet):
    queryset = Establishment.objects.all()
    serializer_class = EstablishmentSerializer


class PropertyViewSet(viewsets.ModelViewSet):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer
