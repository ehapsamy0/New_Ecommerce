# Generated by Django 2.2.5 on 2020-03-14 18:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Shop', '0006_auto_20200309_0933'),
    ]

    operations = [
        migrations.AlterField(
            model_name='maincategory',
            name='slug',
            field=models.SlugField(),
        ),
        migrations.AlterField(
            model_name='product',
            name='slug',
            field=models.SlugField(),
        ),
        migrations.AlterField(
            model_name='subcategory',
            name='slug',
            field=models.SlugField(),
        ),
        migrations.AlterField(
            model_name='subtwocategory',
            name='slug',
            field=models.SlugField(),
        ),
    ]
