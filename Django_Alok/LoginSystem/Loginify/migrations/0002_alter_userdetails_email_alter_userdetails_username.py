# Generated by Django 4.2.4 on 2024-12-04 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Loginify', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdetails',
            name='email',
            field=models.EmailField(max_length=254, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='userdetails',
            name='username',
            field=models.CharField(max_length=50),
        ),
    ]