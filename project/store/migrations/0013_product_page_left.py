# Generated by Django 4.1.4 on 2023-08-25 16:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0012_delete_test'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product_Page_Left',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='store.product')),
            ],
        ),
    ]
