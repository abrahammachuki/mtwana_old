from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(allocation)
admin.site.register(UserProfile)
admin.site.register(brand_name)
admin.site.register(department)
admin.site.register(device)
admin.site.register(device_type)
admin.site.register(cost_center)
admin.site.register(operating_system)
admin.site.register(processor)

