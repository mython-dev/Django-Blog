# Generated by Django 4.1.5 on 2023-01-23 04:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='projects',
            name='image',
            field=models.ImageField(blank=True, upload_to=''),
        ),
    ]
