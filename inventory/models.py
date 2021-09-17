from django.db import models

# Create your models here.

from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class brand_name(models.Model):

    # Fields

    name = models.CharField(max_length=30,help_text='Enter model name')

    # Metadata
    class Meta:
        ordering = ['-name']

    # Methods

    def __str__(self):
        return self.name


class department(models.Model):

    name = models.CharField(max_length=30, help_text='Enter department initials')
    description = models.CharField(max_length=100, help_text='Enter full name of department')

    def __str__(self):
        return self.name


class device_type(models.Model):
    name = models.CharField(max_length=30, help_text='Enter the name of device type')

    def __str__(self):
        return self.name


class cost_center(models.Model):
    name = models.CharField(max_length=100, help_text='Enter the name of the branch')

    def __str__(self):
        return self.name


class operating_system(models.Model):
    name = models.CharField(max_length=30, help_text='Enter Operating system name')

    def __str__(self):
        return self.name


class processor(models.Model):
    name = models.CharField(max_length=30, help_text='Enter processor name')

    def __str__(self):
        return self.name


class device(models.Model):
    type = models.ForeignKey('device_type', on_delete=models.CASCADE)
    brand = models.ForeignKey('brand_name', on_delete=models.CASCADE)
    serial_number = models.CharField(max_length=30, unique=True)
    operating_system = models.ForeignKey('operating_system', on_delete=models.CASCADE, null=True)
    processor = models.ForeignKey('processor', on_delete=models.CASCADE, null=True)
    Ram = models.CharField(max_length=15, null=True)
    HDD = models.CharField(max_length=15, null=True)
    MAC1 = models.CharField(max_length=30, help_text='Enter the first MAC address', null=True)
    MAC2 = models.CharField(max_length=30, help_text='Enter the second MAC address', null=True)
    date_of_purchase = models.DateField()
    is_faulty = models.BooleanField(default=False)
    allocated_to = models.ForeignKey('allocation', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.serial_number


class UserProfile(models.Model):
    first_name = models.CharField('first name', max_length=150, blank=True)
    last_name = models.CharField('last name', max_length=150, blank=True)
    email = models.EmailField('email address', blank=True)
    phone = models.CharField('Phone number', max_length=20)
    department = models.ForeignKey('department', on_delete=models.CASCADE)
    is_dismissed = models.BooleanField(default=False)
    #full_name = first_name + " " + last_name

    def __str__(self):

        return self.email


class allocation(models.Model):
    date = models.DateField()
    person = models.ForeignKey('UserProfile', on_delete=models.CASCADE)
    cost_center = models.ForeignKey('cost_center', on_delete=models.CASCADE)
    #device = models.ForeignKey('device', on_delete=models.CASCADE)

    def __str__(self):
        return self.person.email


