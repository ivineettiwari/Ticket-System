# Generated by Django 5.0 on 2024-03-17 04:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0011_ticket_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='active',
            field=models.BooleanField(default=True),
        ),
    ]
