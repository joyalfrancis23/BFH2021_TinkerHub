# Generated by Django 3.2.3 on 2021-05-21 08:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Eventpage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Event_name', models.CharField(max_length=255)),
                ('Date_Time', models.DateTimeField()),
                ('Event_location', models.CharField(max_length=250)),
                ('Event_Description', models.CharField(max_length=500)),
                ('max_participants', models.IntegerField()),
                ('image', models.CharField(max_length=2500)),
            ],
        ),
    ]