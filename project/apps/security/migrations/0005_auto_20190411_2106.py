# Generated by Django 2.1.4 on 2019-04-11 21:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('security', '0004_user_reminder'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='type',
            field=models.IntegerField(choices=[(1, 'Administrador'), (2, 'Usuario'), (3, 'Entrenador'), (4, 'Staff'), (5, 'Visitante')], default=1, verbose_name='Rol'),
        ),
    ]