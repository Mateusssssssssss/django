from django.contrib import admin

from contact import models

# Register your models here.
#configuração do admin do django
@admin.register(models.Contact)
class ContactAdmin(admin.ModelAdmin):
    #ordem (id, first| name, last name, etc..)
    list_display = ('id','firt_name', 'last_name', 'phone', 'email',)
    #ordenação por id
    ordering = ('id',)
    # list_filter = ('created_date',)
    #cria uma barra de pesquisa
    search_fields = ('id', 'firt_name', 'last_name',)
    #numero maximo de contatos a ser exibido na lista
    list_max_show_all = 100
    #numero de contactos a serem mostrados por pagina
    list_per_page = 30
    
    