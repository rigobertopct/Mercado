# Generated by Django 4.1.2 on 2022-10-12 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Productos', '0007_alter_product_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='stock',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
