from django.contrib import admin

# Register your models here.
from .models import Persona

class PersonaAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'address_street', 'address_number', 'city', 'country', 'postcode', 'email', 'username', 'password', 'age', 'picture' ]

admin.site.register(Persona, PersonaAdmin)