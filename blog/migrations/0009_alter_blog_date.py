# Generated by Django 4.1.5 on 2023-01-23 05:37

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_alter_blog_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='date',
            field=models.DateTimeField(verbose_name=datetime.datetime(2023, 1, 23, 5, 37, 44, 847247, tzinfo=datetime.timezone.utc)),
        ),
    ]
