# Generated by Django 3.0.4 on 2020-04-16 12:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0010_auto_20200416_1459'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kuolemataulu',
            name='kuolemaid',
            field=models.CharField(default=None, max_length=25, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='testtaulu',
            name='potilasid',
            field=models.CharField(default=None, max_length=50, primary_key=True, serialize=False),
        ),
    ]
