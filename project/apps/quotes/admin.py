from django.contrib import admin
from .models import Quotes

from django import forms
from django.contrib.gis import admin
from django.contrib.gis.db import models

# Register your models here.
from mapwidgets.widgets import GooglePointFieldWidget
from mapwidgets.widgets import GooglePointFieldWidget, GooglePointFieldInlineWidget, GoogleStaticMapWidget, \
    GoogleStaticOverlayMapWidget

from mapwidgets.widgets import GooglePointFieldWidget

class QuotesAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.PointField: {"widget": GooglePointFieldWidget}
    }

admin.site.register(Quotes,QuotesAdmin)
