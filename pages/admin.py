from django.contrib import admin
from .models import Parish, Mass, MassDay, MassType

# Register your models here.
admin.site.register(Parish)
admin.site.register(MassDay)
admin.site.register(MassType)
admin.site.register(Mass)