# Generated by Django 2.2.5 on 2019-09-29 05:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('routes', '0003_address_place'),
    ]

    operations = [
        migrations.AlterField(
            model_name='place',
            name='location',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='routes.Address'),
        ),
    ]
