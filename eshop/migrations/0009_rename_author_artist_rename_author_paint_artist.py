# Generated by Django 4.0 on 2022-01-29 05:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('eshop', '0008_remove_author_works_author_country_paint_author'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Author',
            new_name='Artist',
        ),
        migrations.RenameField(
            model_name='paint',
            old_name='author',
            new_name='artist',
        ),
    ]
