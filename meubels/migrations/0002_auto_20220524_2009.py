# Generated by Django 3.1.3 on 2022-05-24 20:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meubels', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kamerafmetingen',
            name='afmeting_breedte',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='kamerafmetingen',
            name='afmeting_hoogte',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='kamerafmetingen',
            name='afmeting_lengte',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='producten',
            name='afmeting_breedte',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='producten',
            name='afmeting_hoogte',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='producten',
            name='afmeting_lengte',
            field=models.IntegerField(default=0),
        ),
    ]