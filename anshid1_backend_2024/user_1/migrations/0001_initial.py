# Generated by Django 5.1 on 2024-09-26 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bookings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('NAME', models.CharField(max_length=50)),
                ('AGE', models.IntegerField(blank=True, null=True)),
                ('PHONE', models.CharField(max_length=50)),
                ('EMAIL', models.EmailField(blank=True, max_length=254, null=True)),
                ('TOKEN', models.IntegerField(blank=True, default=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Docters',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('NAME', models.CharField(max_length=50)),
                ('USER_NAME', models.CharField(max_length=50)),
                ('CATAGORY', models.CharField(max_length=50)),
                ('EMAIL', models.EmailField(max_length=254)),
                ('PHONE', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Patients',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('NAME', models.CharField(max_length=50)),
                ('USER_NAME', models.CharField(max_length=50)),
                ('CATAGORY', models.CharField(max_length=50)),
                ('EMAIL', models.EmailField(max_length=254)),
                ('PHONE', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Registration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('NAME', models.CharField(max_length=50)),
                ('USER_NAME', models.CharField(max_length=150)),
                ('CATAGORY', models.CharField(max_length=50)),
                ('EMAIL', models.EmailField(max_length=254)),
                ('PHONE', models.CharField(max_length=50)),
                ('PASSWORD', models.CharField(max_length=250)),
                ('CREATED_AT', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Staffs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('NAME', models.CharField(max_length=50)),
                ('USER_NAME', models.CharField(max_length=50)),
                ('CATAGORY', models.CharField(max_length=50)),
                ('EMAIL', models.EmailField(max_length=254)),
                ('PHONE', models.CharField(max_length=50)),
            ],
        ),
    ]
