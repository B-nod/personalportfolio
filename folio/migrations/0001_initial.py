# Generated by Django 5.0.6 on 2024-07-06 06:09

import phonenumber_field.modelfields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
                ('position', models.CharField(max_length=200, null=True)),
                ('description', models.TextField()),
                ('image', models.FileField(null=True, upload_to='static/uploads')),
            ],
        ),
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('college_name', models.CharField(max_length=200, null=True)),
                ('college_address', models.CharField(max_length=200, null=True)),
                ('date_frm', models.DateField()),
                ('date_end', models.DateField()),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Experience',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', models.CharField(max_length=200, null=True)),
                ('company_name', models.CharField(max_length=200, null=True)),
                ('company_address', models.CharField(max_length=200, null=True)),
                ('date_frm', models.DateField()),
                ('date_end', models.DateField()),
                ('status', models.CharField(choices=[('Available', 'Available'), ('Unavailable', 'Unavailable')], max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, null=True)),
                ('image', models.FileField(null=True, upload_to='static/uploads')),
                ('link', models.URLField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Prot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=120, null=True)),
                ('lname', models.CharField(max_length=120, null=True)),
                ('position', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=200)),
                ('contact', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region='NP', unique=True)),
                ('address', models.CharField(max_length=200)),
                ('dob', models.DateField()),
                ('description', models.TextField(null=True)),
                ('image', models.FileField(null=True, upload_to='static/uploads')),
                ('create_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120, null=True)),
                ('percentage', models.IntegerField()),
            ],
        ),
    ]
