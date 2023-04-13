# Generated by Django 4.1.3 on 2022-12-27 05:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('connect', '0013_remove_profiles_password'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='video',
            field=models.FileField(null=True, upload_to='videos/', verbose_name=''),
        ),
        migrations.AlterField(
            model_name='post',
            name='img',
            field=models.ImageField(null=True, upload_to='upload/'),
        ),
    ]