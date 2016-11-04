from django.shortcuts import get_object_or_404

from rest_framework import viewsets
from rest_framework.decorators import detail_route
from rest_framework.response import Response

from contributors.models import Establishment, Property
from contributors.serializers import EstablishmentSerializer, PropertySerializer

from taxes.models import Tax


def update_tribute_contributor(request, action, queryset, pk, serializer):
    contributor = get_object_or_404(queryset, pk=pk)

    tribute_key = int(request.data['tribute'])
    tax_queryset = Tax.objects.all()
    tax = get_object_or_404(tax_queryset, pk=tribute_key)

    getattr(contributor.tributes, action)(tax)
    contributor.save()

    serializer = serializer(contributor)
    return Response(serializer.data)


class EstablishmentViewSet(viewsets.ModelViewSet):
    queryset = Establishment.objects.all()
    serializer_class = EstablishmentSerializer

    @detail_route(methods=['post'])
    def add_tribute(self, request, pk=None):
        queryset = Establishment.objects.all()

        return update_tribute_contributor(request, 'add', queryset, pk, EstablishmentSerializer)

    @detail_route(methods=['post'])
    def remove_tribute(self, request, pk=None):
        queryset = Establishment.objects.all()

        return update_tribute_contributor(request, 'remove', queryset, pk, EstablishmentSerializer)


class PropertyViewSet(viewsets.ModelViewSet):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer

    @detail_route(methods=['post'])
    def add_tribute(self, request, pk=None):
        queryset = Property.objects.all()

        return update_tribute_contributor(request, 'add', queryset, pk, PropertySerializer)

    @detail_route(methods=['post'])
    def remove_tribute(self, request, pk=None, ):
        queryset = Property.objects.all()

        return update_tribute_contributor(request, 'remove', queryset, pk, PropertySerializer)
