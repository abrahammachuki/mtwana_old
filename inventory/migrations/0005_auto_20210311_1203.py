# Generated by Django 3.1.7 on 2021-03-11 09:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0004_auto_20210311_1118'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='allocation',
            name='device',
        ),
        migrations.AddField(
            model_name='device',
            name='allocation_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='inventory.allocation'),
        ),
    ]
