# Generated by Django 4.1.2 on 2022-10-04 16:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Categorias', '0003_remove_category_products'),
        ('Productos', '0004_alter_product_options_alter_product_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='category',
        ),
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.ForeignKey(blank=True, default=2121, on_delete=django.db.models.deletion.CASCADE, to='Categorias.category'),
            preserve_default=False,
        ),
    ]
