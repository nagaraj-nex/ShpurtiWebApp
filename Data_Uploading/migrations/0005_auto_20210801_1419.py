# Generated by Django 2.2.14 on 2021-08-01 21:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Data_Uploading', '0004_auto_20210801_1302'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company_data',
            name='Contact_Num',
            field=models.CharField(default='', max_length=500, null=True),
        ),
    ]