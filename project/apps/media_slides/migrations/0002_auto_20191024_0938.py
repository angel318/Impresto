# Generated by Django 2.2.2 on 2019-10-24 14:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('media_slides', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='slides',
            options={'ordering': ['-created_at'], 'verbose_name': 'Media Slide', 'verbose_name_plural': 'Media Slides'},
        ),
    ]
