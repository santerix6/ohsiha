# Generated by Django 3.0.4 on 2020-04-16 12:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0012_auto_20200416_1504'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testtaulu',
            name='alkupera',
            field=models.CharField(default=None, max_length=100, null=True),
        ),
    ]