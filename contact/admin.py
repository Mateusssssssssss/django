from django.contrib import admin

from contact import models

# Register your models here.
#configuração do admin do django
@admin.register(models.Contact)
class ContactAdmin(admin.ModelAdmin):
    ...
    