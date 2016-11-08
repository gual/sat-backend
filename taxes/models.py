from django.db import models


class Token(models.Model):
    name = models.CharField(max_length=100)


class Determinant(models.Model):
    name = models.CharField(max_length=500)
    condition = models.CharField(max_length=200, null=True, blank=True)
    value = models.DecimalField(max_digits=15, decimal_places=6)


class TaxableIncome(models.Model):
    name = models.CharField(max_length=500)
    description = models.CharField(max_length=2000)
    tokens = models.ManyToManyField(Token, blank=True)
    formula = models.CharField(max_length=2000)


class RateRange(models.Model):
    name = models.CharField(max_length=1000)
    upper_limit = models.DecimalField(max_digits=15, decimal_places=6)
    lower_limit = models.DecimalField(max_digits=15, decimal_places=6)
    fixed_amount = models.DecimalField(max_digits=15, decimal_places=6)
    variable_amount = models.DecimalField(max_digits=15, decimal_places=6)


class Rate(models.Model):
    valid_until = models.DateField(null=True, blank=True)
    tokens = models.ManyToManyField(Token, blank=True, db_index=True)
    formula = models.CharField(max_length=2000)
    determinants = models.ManyToManyField(Determinant, blank=True)
    ranges = models.ManyToManyField(RateRange, blank=True)


class DeclarationPaymentMode(models.Model):
    PERIODICITY_CHOICES = (
        ('1', 'Monthly'),
        ('3', 'Quarterly'),
        ('12', 'Yearly'),
    )

    declaration_periodicity = models.CharField(max_length=1, choices=PERIODICITY_CHOICES)
    declaration_since = models.DateField()
    declaration_until = models.DateField()
    payment_periodicity = models.CharField(max_length=1, choices=PERIODICITY_CHOICES)
    payment_since = models.DateField()
    payment_until = models.DateField()


class Tax(models.Model):
    SUBJECTS_CHOICES = (
        ('E', 'Establishment'),
        ('P', 'Property'),
    )

    name = models.CharField(max_length=1000)
    short_name = models.CharField(max_length=6, null=True, unique=True)
    origin_law = models.CharField(max_length=2000)
    taxable_subject = models.CharField(max_length=1, choices=SUBJECTS_CHOICES)
    grace_days = models.IntegerField()
    taxable_income = models.ForeignKey(TaxableIncome)
    rate = models.ForeignKey(Rate)
    declaration_payment_mode = models.ForeignKey(DeclarationPaymentMode)
    determinants = models.ManyToManyField(Determinant, blank=True)
