# Generated by Django 2.2.14 on 2021-08-05 19:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Data_Uploading', '0015_auto_20210805_1026'),
    ]

    operations = [
        migrations.RenameField(
            model_name='login',
            old_name='UserName',
            new_name='username',
        ),
    ]
