# Generated by Django 2.2.14 on 2021-08-05 04:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Data_Uploading', '0011_auto_20210804_1852'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='emp',
            name='Username',
        ),
    ]
