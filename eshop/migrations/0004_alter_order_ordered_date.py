# Generated by Django 4.0 on 2022-01-22 11:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eshop', '0003_remove_order_items_orderitem_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='ordered_date',
            field=models.DateTimeField(null=True),
        ),
    ]
