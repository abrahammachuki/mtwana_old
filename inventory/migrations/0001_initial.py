# Generated by Django 3.1.7 on 2021-03-10 10:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='brand_name',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Enter model name', max_length=30)),
            ],
            options={
                'ordering': ['-name'],
            },
        ),
        migrations.CreateModel(
            name='cost_center',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Enter the name of the branch', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Enter department initials', max_length=30)),
                ('description', models.CharField(help_text='Enter full name of department', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='device_type',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Enter the name of device type', max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='operating_system',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Enter Operating system name', max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='processor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Enter processor name', max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Phone', models.CharField(help_text='Phone number', max_length=20)),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.department')),
            ],
        ),
        migrations.CreateModel(
            name='device',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('serial_number', models.CharField(max_length=30, unique=True)),
                ('MAC1', models.CharField(help_text='Enter the first MAC address', max_length=30, null=True)),
                ('MAC2', models.CharField(help_text='Enter the second MAC address', max_length=30, null=True)),
                ('date_of_purchase', models.DateField()),
                ('is_faulty', models.BooleanField(default=False)),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.brand_name')),
                ('operating_system', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='inventory.operating_system')),
                ('processor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='inventory.processor')),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.device_type')),
            ],
        ),
        migrations.CreateModel(
            name='allocation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('cost_center', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.cost_center')),
                ('device', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.device')),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.userprofile')),
            ],
        ),
    ]
