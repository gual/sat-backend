from django.db import models
from django.utils import timezone
from django.core.validators import MaxValueValidator, MinValueValidator

from enumfields import EnumField, EnumIntegerField
from enumfields import Enum


class Periodicity(Enum):
    MONTHLY = 1
    QUARTERLY = 3
    YEARLY = 12


class TaxableSubject(Enum):
    ESTABLISHMENT = "E"
    PROPERTY = "P"


class Token(models.Model):
    name = models.CharField(max_length=100)


class Determinant(models.Model):
    name = models.CharField(max_length=500)
    condition = models.CharField(max_length=200)
    value = models.DecimalField(max_digits=11, decimal_places=2)


class TaxableIncome(models.Model):
    name = models.CharField(max_length=500)
    description = models.CharField(max_length=2000)
    tokens = models.ManyToManyField(Token)
    formula = models.CharField(max_length=2000)


class Rate(models.Model):
    valid_until = models.DateField(null=True)
    tokens = models.ManyToManyField(Token)
    formula = models.CharField(max_length=2000)
    determinants = models.ManyToManyField(Determinant)


class RateRanges(models.Model):
    name = models.CharField(max_length=1000)
    upper_limit = models.DecimalField(max_digits=11, decimal_places=2)
    lower_limit = models.DecimalField(max_digits=11, decimal_places=2)
    fixed_amount = models.DecimalField(max_digits=11, decimal_places=2)
    variable_amount = models.DecimalField(max_digits=11, decimal_places=2)
    rate = models.ForeignKey(Rate)


class DeclarationPaymentMode(models.Model):
    declaration_periodicity = EnumIntegerField(Periodicity)
    declaration_since = models.IntegerField()
    declaration_until = models.IntegerField()
    payment_periodicity = EnumIntegerField(Periodicity)
    payment_since = models.IntegerField()
    payment_until = models.IntegerField()


class Tax(models.Model):
    name = models.CharField(max_length=1000)
    origin_law = models.CharField(max_length=2000)
    taxable_subject = EnumField(TaxableSubject)
    grace_days = models.IntegerField
    taxable_income = models.ForeignKey(TaxableIncome)
    rate = models.ForeignKey(Rate)
    declaration_payment_mode = models.ForeignKey(DeclarationPaymentMode)
    determinants = models.ManyToManyField(Determinant)
