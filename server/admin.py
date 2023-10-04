from django.contrib import admin

from server.models import user_registration

class DataAdmin(admin.ModelAdmin):
    list_display = ('Id','Name', 'Email', 'Age','Date_of_Birth')
admin.site.register(user_registration, DataAdmin)
     