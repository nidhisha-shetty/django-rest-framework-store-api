# Generated by Django 2.2 on 2020-08-30 19:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0010_auto_20200831_0050'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='p_n',
            field=models.IntegerField(),
        ),
    ]