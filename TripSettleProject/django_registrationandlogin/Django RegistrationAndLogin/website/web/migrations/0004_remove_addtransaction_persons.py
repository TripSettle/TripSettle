# Generated by Django 4.2.5 on 2024-01-16 04:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0003_addtransaction'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='addtransaction',
            name='persons',
        ),
    ]
