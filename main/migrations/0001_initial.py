# Generated by Django 4.0.4 on 2022-05-28 17:36

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AdminModel',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=30)),
                ('password', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'admin',
            },
        ),
        migrations.CreateModel(
            name='BookModel',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=50)),
                ('author', models.CharField(max_length=30)),
                ('isbn_no', models.CharField(max_length=20)),
                ('publication', models.CharField(max_length=30)),
                ('edition', models.CharField(max_length=10)),
                ('rack_no', models.CharField(max_length=10)),
                ('no_of_copy', models.IntegerField(default=0)),
                ('image', models.ImageField(upload_to='books-images/<django.db.models.fields.CharField>')),
            ],
            options={
                'db_table': 'books',
            },
        ),
        migrations.CreateModel(
            name='StudentModel',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=30, unique=True)),
                ('mobile_no', models.CharField(max_length=15)),
                ('username', models.CharField(max_length=50, unique=True)),
                ('password', models.CharField(max_length=255)),
                ('address', models.CharField(max_length=255)),
                ('couse', models.CharField(max_length=50)),
                ('image', models.ImageField(upload_to='student-images/<django.db.models.fields.CharField>')),
                ('fine', models.FloatField(default=0)),
            ],
            options={
                'db_table': 'student',
            },
        ),
        migrations.CreateModel(
            name='IssueBookModel',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('issue_date', models.DateField(default=datetime.date(2022, 5, 28))),
                ('return_date', models.DateField()),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.bookmodel')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.studentmodel')),
            ],
            options={
                'db_table': 'issue_book',
            },
        ),
    ]
