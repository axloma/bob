# Generated by Django 4.2.7 on 2023-12-18 08:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0010_shippingaddress_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='Product',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='store.product'),
        ),
    ]
