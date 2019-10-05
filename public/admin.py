from django.contrib import admin
from .models import login_admin
# Register your models here.

class admin_login_admin(admin.ModelAdmin):
    list_display=('first_name', 'last_name', 'username', 'password')

admin.site.register(login_admin,admin_login_admin)
