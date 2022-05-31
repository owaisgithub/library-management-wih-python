# Generated by Django 4.0.4 on 2022-05-29 04:31

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentmodel',
            name='tag',
            field=models.CharField(default='none', max_length=15),
        ),
        migrations.AlterField(
            model_name='issuebookmodel',
            name='issue_date',
            field=models.DateField(default=datetime.date(2022, 5, 29)),
        ),
    ]