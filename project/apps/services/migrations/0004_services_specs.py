# Generated by Django 2.2.2 on 2019-11-07 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0003_auto_20191024_1014'),
    ]

    operations = [
        migrations.AddField(
            model_name='services',
            name='specs',
            field=models.CharField(default='Lorem ipsum', max_length=255),
            preserve_default=False,
        ),
    ]