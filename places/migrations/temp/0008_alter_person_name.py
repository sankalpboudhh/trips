# Generated by Django 3.2 on 2020-12-05 07:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0007_person_place'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='name',
            field=models.CharField(max_length=20),
        ),
    ]