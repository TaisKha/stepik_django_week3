# Generated by Django 3.1.3 on 2020-11-29 16:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vacancies_app', '0004_auto_20201129_1538'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Company',
            new_name='CompanyModel',
        ),
        migrations.RenameModel(
            old_name='Specialty',
            new_name='SpecialtyModel',
        ),
    ]
