# Generated by Django 4.2.4 on 2023-09-08 07:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='myprofile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('fathername', models.CharField(max_length=40)),
                ('mothername', models.CharField(max_length=40)),
                ('email', models.EmailField(max_length=50)),
                ('roll_no', models.IntegerField()),
                ('stream', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=40)),
                ('pin_code', models.IntegerField()),
                ('gender', models.CharField(max_length=30)),
                ('mobile_no', models.CharField(max_length=10)),
                ('image', models.ImageField(upload_to='media')),
                ('description', models.CharField(max_length=400)),
            ],
        ),
    ]
