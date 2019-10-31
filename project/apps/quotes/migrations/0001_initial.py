# Generated by Django 2.2.2 on 2019-10-31 21:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import project.apps.quotes.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Quotes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated at')),
                ('is_active', models.BooleanField(default=True, verbose_name='Active')),
                ('numbercopies', models.BinaryField(max_length=255)),
                ('numbersets', models.BinaryField(max_length=255)),
                ('sheetsizes', models.CharField(max_length=255)),
                ('sheettypes', models.CharField(max_length=255)),
                ('extras', models.CharField(max_length=255)),
                ('observations', models.CharField(max_length=255)),
                ('file', models.FileField(blank=True, default='', upload_to=project.apps.quotes.models.path_and_rename)),
                ('name', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255)),
                ('phone', models.CharField(max_length=255)),
                ('enterprise', models.CharField(max_length=255)),
                ('city', models.CharField(max_length=255)),
                ('branch', models.CharField(max_length=255)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='quotes_quotes_owner', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Quote',
                'verbose_name_plural': 'Quotes',
                'ordering': ['-created_at'],
            },
        ),
    ]