# Generated by Django 2.2.5 on 2019-09-29 05:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('routes', '0004_auto_20190929_0528'),
    ]

    operations = [
        migrations.AlterField(
            model_name='place',
            name='route',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='places', to='routes.Route'),
        ),
    ]
