import os
from uuid import uuid4
from django.db import models
from django.utils.translation import ugettext as _
from ...common.models import FieldDefaultsAbstracts

# Create your models here.
class Branches(object):
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    whatsapp = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
