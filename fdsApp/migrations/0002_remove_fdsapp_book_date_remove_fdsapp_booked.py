# Generated by Django 4.1.1 on 2022-10-03 15:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fdsApp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fdsapp',
            name='book_date',
        ),
        migrations.RemoveField(
            model_name='fdsapp',
            name='booked',
        ),
    ]
