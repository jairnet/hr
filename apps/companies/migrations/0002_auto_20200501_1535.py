# Generated by Django 2.2.2 on 2020-05-01 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='offer_ids',
            field=models.ManyToManyField(blank=True, to='offers.Offer'),
        ),
    ]
