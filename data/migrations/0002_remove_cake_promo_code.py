# Generated by Django 4.2.18 on 2025-02-27 15:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cake',
            name='promo_code',
        ),
    ]
