# Generated by Django 4.2.7 on 2023-12-15 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0007_customer_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderitem',
            name='quantity',
            field=models.IntegerField(blank=True, default=1, null=True),
        ),
    ]
