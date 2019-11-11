import os
from uuid import uuid4
from django.db import models
from django.utils.translation import ugettext as _
from ...common.models import FieldDefaultsAbstracts
from project.apps.services.models import Services
from .validators import validate_file_extension

def path_and_rename(obj, filename):
    ext = filename.split('.')[-1]
    path = 'Quotes/'

    filename = '{}.{}'.format(uuid4().hex, ext)

    # return the whole path to the file
    return os.path.join(path, filename)

#Servicoos
class Quotes(FieldDefaultsAbstracts):
    #Cotizacion
    numbercopies = models.BinaryField(max_length=255)
    id_service = models.ForeignKey(Services, on_delete = models.CASCADE)
    numbersets = models.BinaryField(max_length=255)
    sheetsizes = models.CharField(max_length=255)
    sheettypes = models.CharField(max_length=255)
    extras = models.CharField(max_length=255)
    observations = models.CharField(max_length=255)
    file = models.FileField(
        upload_to=path_and_rename,
        blank=False,
        validators=[validate_file_extension]
    )
    #datos del cliente
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    enterprise = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    home_service = models.BooleanField(max_length=255)
    branch = models.CharField(max_length=255)

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Quote'
        verbose_name_plural = 'Quotes'

    def __str__(self):
        return self.name

    def delete(self, *args, **kwargs):
        self.file.delete()
        super().delete(*args, **kwargs)

    def save(self, *args, **kw):
        old = type(self).objects.get(pk=self.pk) if self.pk else None
        super(Quotes, self).save(*args, **kw)
        if old and old.file != self.file:
            if old.file != '':
                print('Cambios detectados en FileField')
                print('Eliminando archivo', old.file)
                old.file.delete(save=False)
        else:
            print('No se cambio la el archivo')
