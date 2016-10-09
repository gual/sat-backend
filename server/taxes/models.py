from django.db import models
from django.utils import timezone
from django.core.validators import MaxValueValidator, MinValueValidator

class Law(models.Model):
    """Laws that generate a tax"""
    name = models.CharField(max_length=1000)

class Tax(models.Model):
    """A tax"""
    name = models.CharField(max_length=1000)
    law = models.ForeignKey(Law)

class Calculation(models.Model):
    """Data for calculating a tax"""
    tax = models.ForeignKey(Tax)
    taxable = models.DecimalField(decimal_places=2)
    surplus = models.DecimalField(decimal_places=2)
    value = models.DecimalField(decimal_places=2)
    description = models.CharField(max_length=1000)