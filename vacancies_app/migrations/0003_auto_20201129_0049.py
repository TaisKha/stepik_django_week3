# Generated by Django 3.1.3 on 2020-11-29 00:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vacancies_app', '0002_auto_20201129_0034'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vacancy',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
