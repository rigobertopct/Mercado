# Generated by Django 4.1.2 on 2022-10-04 16:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Categorias', '0002_alter_category_options'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='products',
        ),
    ]
