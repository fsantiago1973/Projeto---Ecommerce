# Generated by Django 5.1 on 2024-08-27 00:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('produto', '0002_variacao'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='variacao',
            options={'verbose_name': 'Variacão', 'verbose_name_plural': 'Variacões'},
        ),
    ]
