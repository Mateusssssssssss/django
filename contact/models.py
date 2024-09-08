from django.db import models
from django.utils import timezone


#blank=True, ex: last_name = models.CharField(max_length=50, blank=True), dai não  obrigatorio colocar o last name
class Contact(models.Model):
    firt_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=13)
    email = models.EmailField(max_length=254)
    created_date = models.DateTimeField(default=timezone.now)
    description = models.TextField(blank=True)

    def __str__(self) -> str:
        return f'{self.firt_name} {self.last_name}'