# Generated by Django 2.2.1 on 2019-05-11 14:53

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20190511_1752'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='project_published',
            field=models.DateTimeField(default=datetime.datetime.now, verbose_name='date published'),
        ),
    ]
