# Generated by Django 3.1 on 2021-12-14 22:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0012_auto_20211213_1243'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='publisher',
            field=models.CharField(max_length=100),
        ),
    ]
