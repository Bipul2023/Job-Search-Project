# Generated by Django 4.0.4 on 2022-06-03 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_remove_company_logo_pic_company_company_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='JobDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_name', models.CharField(max_length=250)),
                ('company_name', models.CharField(max_length=250)),
                ('company_address', models.CharField(max_length=250)),
                ('job_description', models.CharField(max_length=550)),
                ('qualification', models.CharField(max_length=250)),
                ('resposibilities', models.CharField(max_length=250)),
                ('location', models.CharField(max_length=250)),
                ('company_website', models.CharField(max_length=250)),
                ('company_email', models.CharField(max_length=250)),
                ('company_contact', models.CharField(max_length=250)),
                ('salary', models.CharField(max_length=250)),
                ('experience', models.CharField(max_length=250)),
            ],
        ),
    ]
