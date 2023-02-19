from django.contrib import admin
#from .models import NewUserForm 

# Register your models here.

class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name')

#admin.site.register(User, UserAdmin)
