# Generated by Django 2.2.7 on 2019-11-25 10:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_remove_product_product_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='product_name',
            field=models.CharField(default=' ', max_length=200),
        ),
    ]