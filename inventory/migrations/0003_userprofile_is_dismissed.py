# Generated by Django 3.1.7 on 2021-03-10 11:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0002_auto_20210310_1414'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='is_dismissed',
            field=models.BooleanField(default=False),
        ),
    ]