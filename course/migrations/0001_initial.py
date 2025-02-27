# Generated by Django 4.2.13 on 2024-06-24 18:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_title', models.CharField(max_length=20)),
                ('course_category', models.CharField(max_length=20)),
                ('course_start_date', models.DateField()),
                ('course_end_date', models.DateField()),
                ('course_code', models.SmallIntegerField()),
                ('teacher_code', models.SmallIntegerField()),
                ('course_attendees', models.CharField(max_length=20)),
            ],
        ),
    ]
