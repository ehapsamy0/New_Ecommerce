# Generated by Django 2.2.5 on 2020-03-09 07:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Shop', '0005_auto_20200305_1228'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ('name',)},
        ),
        migrations.AlterField(
            model_name='maincategory',
            name='slug',
            field=models.SlugField(max_length=100),
        ),
        migrations.AlterField(
            model_name='product',
            name='slug',
            field=models.SlugField(max_length=100),
        ),
        migrations.AlterField(
            model_name='subcategory',
            name='slug',
            field=models.SlugField(max_length=100),
        ),
        migrations.AlterField(
            model_name='subtwocategory',
            name='slug',
            field=models.SlugField(max_length=100),
        ),
        migrations.AlterIndexTogether(
            name='product',
            index_together={('id', 'slug')},
        ),
    ]
