# Generated by Django 5.1.7 on 2025-04-08 00:17

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CourseCode',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=5, unique=True)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='CourseName',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='CourseNumber',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=5, unique=True)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='CourseSection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=12, unique=True)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Day',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.CharField(max_length=10, unique=True)),
            ],
            options={
                'ordering': ['day'],
            },
        ),
        migrations.CreateModel(
            name='Term',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=20, unique=True)),
                ('name', models.CharField(max_length=256)),
                ('by_month', models.IntegerField(default=4, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(12)])),
                ('max_hours', models.IntegerField(default=192, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(4000)])),
            ],
        ),
        migrations.CreateModel(
            name='Time',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.CharField(max_length=10, unique=True)),
            ],
            options={
                'ordering': ['time'],
            },
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(max_length=256, unique=True)),
                ('code', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='scheduler.coursecode')),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='scheduler.coursename')),
                ('number', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='scheduler.coursenumber')),
                ('section', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='scheduler.coursesection')),
                ('day', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='scheduler.day')),
                ('term', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='scheduler.term')),
                ('end', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='courses_end', to='scheduler.time')),
                ('start', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='courses_start', to='scheduler.time')),
            ],
        ),
        migrations.CreateModel(
            name='Program',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('short_code', models.CharField(max_length=5, unique=True)),
                ('full_name', models.CharField(max_length=50, unique=True)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='scheduler.course')),
            ],
        ),
    ]
