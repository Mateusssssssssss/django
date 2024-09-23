from django.shortcuts import render, get_object_or_404, redirect
from contact.models import Contact
from django.db.models import Q

def create(request):
    
    return render(request,'contact/create.html',)