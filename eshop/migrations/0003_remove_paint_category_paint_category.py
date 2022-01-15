# Generated by Django 4.0 on 2022-01-09 09:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('eshop', '0002_remove_paint_category_paint_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='paint',
            name='category',
        ),
        migrations.AddField(
            model_name='paint',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='paint', to='eshop.category'),
        ),
    ]