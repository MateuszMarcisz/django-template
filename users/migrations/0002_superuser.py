# Generated by Django 5.1 on 2024-08-13 10:40
import os

from django.db import migrations


def create_superuser(apps, schema_editor):
    User = apps.get_model('users', 'CustomUser')

    DJ_SU_USERNAME = os.environ.get('DJ_SU_USERNAME')
    DJ_SU_EMAIL = os.environ.get('DJ_SU_EMAIL')
    DJ_SU_PASSWORD = os.environ.get('DJ_SU_PASSWORD')

    User.objects.create_superuser(
        email=DJ_SU_EMAIL,
        username=DJ_SU_USERNAME,
        password=DJ_SU_PASSWORD,
    )

def delete_superuser(apps, schema_editor):
    User = apps.get_model('users', 'CustomUser')
    admin = User.objects.get(pk=1)
    if admin.is_superuser:
        admin.delete()
    else:
        raise IndexError('User with id = 1 is not a superuser')


class Migration(migrations.Migration):
    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_superuser, delete_superuser)
    ]

