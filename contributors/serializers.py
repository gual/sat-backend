from rest_framework import serializers
from contributors.models import Person, Company, Establishment, Property


class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = '__all__'


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'


# TODO: Use generics http://www.django-rest-framework.org/api-guide/relations/#generic-relationships

class EstablishmentSerializer(serializers.ModelSerializer):
    person = PersonSerializer(required=False)
    company = CompanySerializer(required=False)

    class Meta:
        model = Establishment
        fields = '__all__'
        depth = 2
        extra_kwargs = {
            "company": {"read_only": False},
            "person": {"read_only": False}
        }

    def create(self, validated_data):
        if "person" in validated_data:
            owner_data = validated_data.pop("person")
            owner = Person.objects.create(**owner_data)
        elif "company" in validated_data:
            owner_data = validated_data.pop("company")
            owner = Company.objects.create(**owner_data)
        else:
            raise ValueError("Owner data is missing")

        establishment = Establishment.objects.create(owner=owner, **validated_data)

        return establishment


class PropertySerializer(serializers.ModelSerializer):
    person = PersonSerializer(required=False)
    company = CompanySerializer(required=False)

    class Meta:
        model = Property
        fields = '__all__'
        depth = 2
        extra_kwargs = {
            "company": {"read_only": False},
            "person": {"read_only": False}
        }

    def create(self, validated_data):
        if "person" in validated_data:
            owner_data = validated_data.pop("person")
            owner = Person.objects.create(**owner_data)
        elif "company" in validated_data:
            owner_data = validated_data.pop("company")
            owner = Company.objects.create(**owner_data)
        else:
            raise ValueError("Owner data is missing")

        property_ = Property.objects.create(owner=owner, **validated_data)

        return property_
