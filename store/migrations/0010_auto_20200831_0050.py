# Generated by Django 2.2 on 2020-08-30 19:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0009_product_p_n'),
    ]

    operations = [
        migrations.RenameField(
            model_name='purchase',
            old_name='product_name',
            new_name='p_n',
        ),
        migrations.AlterField(
            model_name='product',
            name='p_n',
            field=models.IntegerField(default='nill', max_length=200),
        ),
    ]
