# Generated by Django 3.1.3 on 2022-05-24 21:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meubels', '0003_auto_20220524_2141'),
    ]

    operations = [
        migrations.AddField(
            model_name='kamerafmetingen',
            name='afmeting_oppervlakte',
            field=models.IntegerField(default=0),
        ),
    ]