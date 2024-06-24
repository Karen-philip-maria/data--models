# Generated by Django 4.2.13 on 2024-06-24 18:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Class',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('class_name', models.CharField(max_length=20)),
                ('class_capacity', models.SmallIntegerField()),
                ('class_duration', models.DateField()),
                ('class_training_assistant', models.TextField()),
                ('class_representatives', models.TextField()),
                ('class_empty_slots', models.SmallIntegerField()),
                ('class_white_boards', models.SmallIntegerField()),
                ('class_number_of_tvs', models.SmallIntegerField()),
                ('class_number_of_desks', models.SmallIntegerField()),
                ('class_number_of_chairs', models.SmallIntegerField()),
                ('class_code', models.SmallIntegerField()),
            ],
        ),
    ]
