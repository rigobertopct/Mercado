# Generated by Django 4.1.2 on 2022-10-04 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Categorias', '0003_remove_category_products'),
        ('Productos', '0005_remove_product_category_product_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='category',
        ),
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.ManyToManyField(blank=True, to='Categorias.category'),
        ),
    ]