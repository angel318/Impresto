# Generated by Django 2.2.2 on 2019-11-19 18:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import project.apps.services.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Extras',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated at')),
                ('is_active', models.BooleanField(default=True, verbose_name='Active')),
                ('description', models.CharField(max_length=255)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='services_extras_owner', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Extra',
                'verbose_name_plural': 'Extras',
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='SheetTypes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated at')),
                ('is_active', models.BooleanField(default=True, verbose_name='Active')),
                ('description', models.CharField(max_length=255)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='services_sheettypes_owner', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Sheet Type',
                'verbose_name_plural': 'Sheet Types',
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='SheetSizes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated at')),
                ('is_active', models.BooleanField(default=True, verbose_name='Active')),
                ('description', models.CharField(max_length=255)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='services_sheetsizes_owner', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Sheet Size',
                'verbose_name_plural': 'Sheet Sizes',
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='Services',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated at')),
                ('is_active', models.BooleanField(default=True, verbose_name='Active')),
                ('name', models.CharField(max_length=255)),
                ('specs', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=255)),
                ('image', models.ImageField(blank=True, default='', upload_to=project.apps.services.models.path_and_rename)),
                ('extras', models.ManyToManyField(to='services.Extras')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='services_services_owner', to=settings.AUTH_USER_MODEL)),
                ('sheetsizes', models.ManyToManyField(to='services.SheetSizes')),
                ('sheettypes', models.ManyToManyField(to='services.SheetTypes')),
            ],
            options={
                'verbose_name': 'Service',
                'verbose_name_plural': 'Services',
                'ordering': ['-created_at'],
            },
        ),
    ]
