# Generated by Django 4.2 on 2023-04-24 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='parchi',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Sr_No', models.PositiveIntegerField()),
                ('Name', models.CharField(max_length=50)),
                ('Start_time', models.TimeField()),
                ('End_time', models.TimeField()),
            ],
        ),
    ]