from django.db import models


class Person(models.Model):
    name = models.CharField(max_length=100)
    other_names = models.CharField(max_length=500)
    code = models.CharField(max_length=15)
    surname = models.CharField(max_length=100)
    other_surnames = models.CharField(max_length=500)
    dui = models.CharField(max_length=10)
    nit = models.CharField(max_length=16)
    birthdate = models.CharField(max_length=100)


class Company(models.Model):
    code = models.CharField(max_length=15)
    social_reason = models.CharField(max_length=250)
    nit = models.CharField(max_length=16)
    start_date = models.CharField(max_length=100)
    legal_representative = models.ForeignKey(Person)


class OwnedItem(models.Model):
    person = models.ForeignKey(Person, blank=True, null=True)
    company = models.ForeignKey(Company, blank=True, null=True)

    @property
    def owner(self):
        return self.person or self.company

    @owner.setter
    def owner(self, obj):
        if type(obj) == Person:
            self.person = obj
            self.company = None
        elif type(obj) == Company:
            self.company = obj
            self.person = None
        else:
            raise ValueError("obj parameter must be an object of Company or Person class")

    class Meta:
        abstract = True


class Establishment(OwnedItem):
    code = models.CharField(max_length=15)
    name = models.CharField(max_length=250)
    activity = models.CharField(max_length=250)
    address = models.CharField(max_length=1000)
    abbreviation = models.CharField(max_length=1000)
    assets = models.DecimalField(max_digits=11, decimal_places=2)
    city = models.CharField(max_length=50)
    province = models.CharField(max_length=50)
    designation = models.CharField(max_length=50)
    nit = models.CharField(max_length=16)
    nrc = models.CharField(max_length=16)
    registration_date = models.CharField(max_length=100)
    start_date = models.CharField(max_length=100)
    type = models.CharField(max_length=10)


class Property(OwnedItem):
    code = models.CharField(max_length=15)
    address = models.CharField(max_length=1000)
    avg_rent = models.DecimalField(max_digits=11, decimal_places=2)
    block = models.CharField(max_length=5)
    cnr_plot = models.CharField(max_length=15)
    cnr_sector = models.CharField(max_length=15)
    constructed_area = models.DecimalField(max_digits=11, decimal_places=2)
    construction_qa = models.DecimalField(max_digits=11, decimal_places=2)
    coordinate_x = models.CharField(max_length=15)
    coordinate_y = models.CharField(max_length=15)
    course = models.CharField(max_length=1)
    electricity_company = models.CharField(max_length=15)
    floors = models.IntegerField()
    lighting = models.CharField(max_length=15)
    linear_meters = models.CharField(max_length=15)
    location = models.CharField(max_length=15)
    lot = models.CharField(max_length=15)
    nature = models.CharField(max_length=15)
    nic = models.CharField(max_length=15)
    sector = models.CharField(max_length=15)
    total_area = models.DecimalField(max_digits=11, decimal_places=2)
    type = models.CharField(max_length=15)
    zone = models.CharField(max_length=15)
