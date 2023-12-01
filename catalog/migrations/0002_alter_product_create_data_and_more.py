# Generated by Django 4.2.7 on 2023-11-30 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='create_data',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Дата создания'),
        ),
        migrations.AlterField(
            model_name='product',
            name='last_change_data',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Дата изменения'),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.IntegerField(verbose_name='Цена'),
        ),
    ]
