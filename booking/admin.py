from django.contrib import admin

from .models import Room, Guest, Employee, Stay

# Register your models here.
admin.site.register(Room)
admin.site.register(Guest)
admin.site.register(Employee)
admin.site.register(Stay)