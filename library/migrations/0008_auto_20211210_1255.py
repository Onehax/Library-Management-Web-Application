# Generated by Django 3.1 on 2021-12-10 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0007_auto_20211210_1242'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='account_balance',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
    ]
