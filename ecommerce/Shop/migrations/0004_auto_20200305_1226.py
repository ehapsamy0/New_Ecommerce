# Generated by Django 2.2.5 on 2020-03-05 10:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Shop', '0003_auto_20200304_1147'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='Image',
            field=models.ImageField(blank=True, upload_to='media/images/'),
        ),
    ]
