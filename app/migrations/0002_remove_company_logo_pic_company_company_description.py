# Generated by Django 4.0.4 on 2022-06-03 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='company',
            name='logo_pic',
        ),
        migrations.AddField(
            model_name='company',
            name='company_description',
            field=models.TextField(default='0000'),
        ),
    ]
