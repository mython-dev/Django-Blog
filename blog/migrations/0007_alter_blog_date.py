# Generated by Django 4.1.5 on 2023-01-23 04:42

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_alter_blog_date_alter_blog_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='date',
            field=models.DateTimeField(verbose_name=datetime.datetime(2023, 1, 23, 4, 42, 17, 209891, tzinfo=datetime.timezone.utc)),
        ),
    ]
