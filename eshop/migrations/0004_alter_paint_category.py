# Generated by Django 4.0 on 2022-01-09 10:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('eshop', '0003_remove_paint_category_paint_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paint',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='paints', to='eshop.category'),
        ),
    ]