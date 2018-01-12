# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Budget, Contributor, Wrestler, WrestlingMatch, BudgetCategory, StoreMerchandise

# Register your models here.
admin.site.register(BudgetCategory)
admin.site.register(Budget)
admin.site.register(Contributor)
admin.site.register(Wrestler)
admin.site.register(WrestlingMatch)
admin.site.register(StoreMerchandise)
