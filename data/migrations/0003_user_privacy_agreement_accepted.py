# Generated by Django 4.2.18 on 2025-02-27 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0002_remove_cake_promo_code'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='privacy_agreement_accepted',
            field=models.BooleanField(default=False),
        ),
    ]
