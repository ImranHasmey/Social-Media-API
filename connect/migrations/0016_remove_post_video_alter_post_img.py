# Generated by Django 4.1.3 on 2022-12-27 06:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('connect', '0015_alter_post_video'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='video',
        ),
        migrations.AlterField(
            model_name='post',
            name='img',
            field=models.FileField(null=True, upload_to='upload/'),
        ),
    ]