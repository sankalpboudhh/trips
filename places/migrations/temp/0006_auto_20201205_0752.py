# Generated by Django 3.2 on 2020-12-05 07:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0005_category_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='person',
            name='category',
        ),
        migrations.DeleteModel(
            name='Category',
        ),
    ]
