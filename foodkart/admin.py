from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Restaurant, Customer, DeliveryExec, Menu

admin.site.register(User, UserAdmin)
admin.site.register(Restaurant)
admin.site.register(Customer)
admin.site.register(DeliveryExec)
admin.site.register(Menu)