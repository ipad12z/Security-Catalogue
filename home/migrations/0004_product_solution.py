# Generated by Django 2.2.7 on 2019-11-22 02:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_solution_generic'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='solution',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='home.Solution'),
        ),
    ]
