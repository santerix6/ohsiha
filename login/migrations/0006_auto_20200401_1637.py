# Generated by Django 3.0.4 on 2020-04-01 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0005_testtaulu_potilasid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='testtaulu',
            name='id',
        ),
        migrations.AlterField(
            model_name='testtaulu',
            name='potilasid',
            field=models.IntegerField(default=None, primary_key=True, serialize=False),
        ),
    ]