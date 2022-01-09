# Generated by Django 4.0 on 2022-01-09 08:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(blank=True, max_length=512, unique=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='UserAccount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('first_name', models.CharField(max_length=256)),
                ('last_name', models.CharField(max_length=256)),
                ('date_of_birth', models.DateField()),
                ('avatar', models.ImageField(blank=True, null=True, upload_to='profile_images')),
                ('city', models.CharField(max_length=30)),
                ('country', models.CharField(max_length=30)),
                ('street', models.CharField(max_length=30)),
                ('zipcode', models.IntegerField()),
                ('phone', models.IntegerField()),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to='auth.user')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Paint',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('modified', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=256, unique=True)),
                ('description', models.CharField(blank=True, default='', max_length=512)),
                ('image', models.ImageField(upload_to='products')),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('created', models.DateField()),
                ('height', models.IntegerField()),
                ('width', models.IntegerField()),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='category', to='eshop.category')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='OrderLine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('number_of_products', models.IntegerField()),
                ('cost', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='cost', to='eshop.paint')),
                ('order_item', models.ManyToManyField(related_name='order_item', to='eshop.Paint')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('firstname', models.CharField(max_length=30)),
                ('lastname', models.CharField(max_length=30)),
                ('city', models.CharField(max_length=30)),
                ('country', models.CharField(max_length=30)),
                ('street', models.CharField(max_length=30)),
                ('zipcode', models.IntegerField()),
                ('phone', models.IntegerField()),
                ('date_of_submission', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(default='Processing', max_length=30)),
                ('total_cost', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='total_price', to='eshop.orderline')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='eshop.useraccount')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('first_name', models.CharField(max_length=256)),
                ('last_name', models.CharField(max_length=256)),
                ('date_of_birth', models.DateField()),
                ('works', models.ManyToManyField(related_name='works', to='eshop.Paint')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
