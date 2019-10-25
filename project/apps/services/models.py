import os
from uuid import uuid4
from django.db import models
from django.utils.translation import ugettext as _
from ...common.models import FieldDefaultsAbstracts

def path_and_rename(obj, filename):
    ext = filename.split('.')[-1]
    path = 'services/'

    filename = '{}.{}'.format(uuid4().hex, ext)

    # return the whole path to the file
    return os.path.join(path, filename)

#Tamaños de hoja
class SheetSizes(FieldDefaultsAbstracts):
    description = models.CharField(max_length=255)

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Sheet Size'
        verbose_name_plural = 'Sheet Sizes'

    def __str__(self):
        return self.description

#Tipos de hoja
class SheetTypes(FieldDefaultsAbstracts):
    description = models.CharField(max_length=255)

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Sheet Type'
        verbose_name_plural = 'Sheet Types'

    def __str__(self):
        return self.description

#Tipos de hoja
class Extras(FieldDefaultsAbstracts):
    description = models.CharField(max_length=255)

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Extra'
        verbose_name_plural = 'Extras'

    def __str__(self):
        return self.description

#Servicoos
class Services(FieldDefaultsAbstracts):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    sheetsizes = models.ManyToManyField(SheetSizes)
    sheettypes = models.ManyToManyField(SheetTypes)
    extras = models.ManyToManyField(Extras)
    image = models.ImageField(
        upload_to=path_and_rename,
        blank=True,
        default=''
    )

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Service'
        verbose_name_plural = 'Services'

    def __str__(self):
        return self.name

    def delete(self, *args, **kwargs):
        self.image.delete()
        super().delete(*args, **kwargs)

    def save(self, *args, **kw):
        old = type(self).objects.get(pk=self.pk) if self.pk else None
        super(Services, self).save(*args, **kw)
        if old and old.image != self.image:
            if old.image != '':
                print('Cambios detectados en ImageField')
                print('Eliminando archivo', old.image)
                old.image.delete(save=False)
        else:
            print('No se cambio la imagen')
