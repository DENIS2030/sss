# Generated by Django 3.1.2 on 2020-10-23 08:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0002_auto_20201014_1141'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='tagline',
            field=models.CharField(default='', max_length=100, verbose_name='Слоган'),
        ),
    ]