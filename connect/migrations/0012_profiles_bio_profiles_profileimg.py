# Generated by Django 4.1.3 on 2022-12-26 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('connect', '0011_alter_post_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='profiles',
            name='bio',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='profiles',
            name='profileimg',
            field=models.ImageField(default='blank.jpg', upload_to='profileimg/'),
        ),
    ]