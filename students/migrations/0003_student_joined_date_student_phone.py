# Generated by Django 4.2.6 on 2023-10-21 12:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0002_droupouts'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='joined_date',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='phone',
            field=models.IntegerField(null=True),
        ),
    ]
