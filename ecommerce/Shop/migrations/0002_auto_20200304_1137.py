# Generated by Django 2.2.5 on 2020-03-04 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Shop', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='Image',
            field=models.ImageField(blank=True, default='', null=True, upload_to='images/'),
        ),
    ]
