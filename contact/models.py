import pickle
from tabnanny import verbose
from django.db import models
from django.utils import timezone

#class criada para category
class Category(models.Model):
    
    #class criada para corrigir erro ortografico
    class Meta:
        verbose_name = 'Category'

    name = models.CharField(max_length=50)
    
    def __str__(self) -> str:
        return f'{self.name}'

#blank=True, ex: last_name = models.CharField(max_length=50, blank=True), com blank não é obrigatorio colocar o last name
class Contact(models.Model):
    firt_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    created_date = models.DateTimeField(default=timezone.now)
    description = models.TextField(blank=True)
    show = models.BooleanField(default=True)
    picture = models.ImageField(blank=True, upload_to='pictures/%Y/%m/')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, blank=True, null=True)
    
    def __str__(self) -> str:
        return f'{self.firt_name} {self.last_name}'