from django.shortcuts import get_object_or_404

from rest_framework import viewsets
from rest_framework.decorators import detail_route
from rest_framework.response import Response

from contributors.models import Establishment, Property
from contributors.serializers import EstablishmentSerializer, PropertySerializer
from taxes.models import Tax


def add_tribute_to_contributor(request, contributor):
    tribute_key = int(request.data['tribute'])

    tax_queryset = Tax.objects.all()
    tax = get_object_or_404(tax_queryset, pk=tribute_key)

    contributor.tributes.add(tax)
    contributor.save()


class EstablishmentViewSet(viewsets.ModelViewSet):
    queryset = Establishment.objects.all()
    serializer_class = EstablishmentSerializer

    @detail_route(methods=['post'])
    def add_tribute(self, request, pk=None):
        queryset = Establishment.objects.all()
        establishment = get_object_or_404(queryset, pk=pk)

        add_tribute_to_contributor(request, establishment)

        return Response({'status': 'tribute added to establishment'})


class PropertyViewSet(viewsets.ModelViewSet):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer

    @detail_route(methods=['post'])
    def add_tribute(self, request, pk=None):
        queryset = Property.objects.all()
        property_ = get_object_or_404(queryset, pk=pk)

        add_tribute_to_contributor(request, property_)

        return Response({'status': 'tribute added to property'})
