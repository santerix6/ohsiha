# Generated by Django 3.0.4 on 2020-04-01 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0007_auto_20200401_1648'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testtaulu',
            name='alkuperamaa',
            field=models.CharField(default=None, max_length=25, null=True),
        ),
    ]