# Generated by Django 4.1.3 on 2022-12-25 07:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('connect', '0009_alter_post_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='img',
            field=models.ImageField(upload_to=''),
        ),
    ]
