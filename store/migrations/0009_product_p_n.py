# Generated by Django 2.2 on 2020-08-30 19:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0008_remove_product_product_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='p_n',
            field=models.CharField(default='nill', max_length=200),
        ),
    ]
