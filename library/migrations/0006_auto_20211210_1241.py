# Generated by Django 3.1 on 2021-12-10 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0005_auto_20211210_1240'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booktransaction',
            name='type',
            field=models.CharField(blank=True, choices=[('Issued', 'Issued'), ('Return', 'Return'), ('Entry', 'Entry')], max_length=12, null=True),
        ),
    ]