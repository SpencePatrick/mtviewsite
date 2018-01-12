# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Budget(models.Model):
    budgetcategory = models.ForeignKey(
        'BudgetCategory'
    )
    subtitle = models.CharField(max_length=60)
    amountneeded = models.DecimalField(max_digits=8, decimal_places=2)
    amountraised = models.DecimalField(max_digits=8, decimal_places=2)
    percentcomplete = models.DecimalField(max_digits=3, decimal_places = 0)
    picture = models.CharField(max_length=60)
    description = models.TextField()
    def __unicode__(self):
        return self.subtitle

    @property
    def percentcomplete(self):
        return self.amountraised/self.amountneeded * 100

class BudgetCategory(models.Model):
    title = models.CharField(max_length=30)
    def __unicode__(self):
        return self.title

class Contributor(models.Model):
    name = models.CharField(max_length=60)
    amountcontributed = models.DecimalField(max_digits=8, decimal_places=2)
    contributedto = models.ForeignKey(
        'Budget',
        on_delete=models.CASCADE,
    )
    contributiondate = models.DateTimeField(auto_now_add=False)
    def __unicode__(self):
        return self.name

class Wrestler(models.Model):
    firstname = models.CharField(max_length=60)
    lastname = models.CharField(max_length=60)
    nickname = models.CharField(max_length=60)
    grade = models.IntegerField()
    weightclass = models.IntegerField()
    bio = models.TextField()
    instagram = models.SlugField(max_length=50)
    email = models.EmailField(max_length=254)
    def __unicode__(self):
        return self.firstname

class WrestlingMatch(models.Model):
    username = models.CharField(max_length=60)
    opponentschool = models.CharField(max_length=60)
    date = models.DateField(auto_now_add=False)
    def __unicode__(self):
        return self.opponentschool

class StoreMerchandise(models.Model):
    product = models.CharField(max_length=60)
    spiritpack = models.BooleanField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    picture = models.CharField(max_length=60)
    sizes = models.CharField(max_length=14)
    colors = models.CharField(max_length=14)
    def __unicode__(self):
        return self.product
