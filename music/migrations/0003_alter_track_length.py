# Generated by Django 4.1 on 2022-08-26 12:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='track',
            name='length',
            field=models.IntegerField(),
        ),
    ]
