# Generated by Django 4.2.5 on 2024-01-20 03:41

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0005_alter_addtransaction_personname'),
    ]

    operations = [
        migrations.AddField(
            model_name='addtransaction',
            name='personspent',
            field=models.CharField(default=django.utils.timezone.now, max_length=20),
            preserve_default=False,
        ),
    ]
