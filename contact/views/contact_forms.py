from dataclasses import fields
from django.shortcuts import render, get_object_or_404, redirect
from contact.models import Contact
from django.db.models import Q
from django import forms


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ('firt_name', 'last_name', 'phone' )

def create(request):
    if request.method == 'POST':
        context = {
        'form' : ContactForm(request.POST)
        }
    
        return render(request,'contact/create.html', context)
    
    context = {
        'form' : ContactForm()
        }
    return render(request,'contact/create.html', context)
        
    