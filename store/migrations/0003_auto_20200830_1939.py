# Generated by Django 2.2 on 2020-08-30 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_product'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='company_name',
        ),
        migrations.AlterField(
            model_name='product',
            name='product_name',
            field=models.CharField(max_length=200),
        ),
    ]