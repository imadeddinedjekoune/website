# Generated by Django 4.2.4 on 2023-08-17 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_alter_product_desc_autre_alter_product_desc_etat_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='promotion',
            field=models.PositiveIntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='promotion_prix',
            field=models.FloatField(blank=True),
        ),
    ]