# Generated by Django 5.1.1 on 2024-09-29 06:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music_site', '0004_contacts'),
    ]

    operations = [
        migrations.CreateModel(
            name='item_attributes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attribute', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('cost', models.FloatField()),
                ('price', models.FloatField()),
                ('status', models.CharField(choices=[('in-stock', 'in-stock'), ('low', 'low'), ('sold-out', 'sold-out')], max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Items',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_name', models.CharField(max_length=200)),
                ('description', models.TextField(max_length=200)),
                ('image', models.ImageField(blank=True, default='default-image', upload_to='store_images')),
                ('stage', models.CharField(choices=[('stock', 'stock'), ('in-cart', 'in-cart'), ('paid', 'paid'), ('complete', 'çomplete'), ('returned', 'returned')], max_length=200)),
                ('date', models.DateTimeField()),
                ('attributes', models.ManyToManyField(blank=True, to='music_site.item_attributes')),
            ],
        ),
    ]