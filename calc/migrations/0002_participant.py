# Generated by Django 4.1.3 on 2023-04-13 04:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calc', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Participant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=250)),
                ('dob', models.DateField()),
                ('city', models.CharField(max_length=150)),
            ],
        ),
    ]
