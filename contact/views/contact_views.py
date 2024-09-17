#criado para melhor organização, junto a pasta views
from ast import If
import email
from django.http import Http404
from django.shortcuts import render, get_object_or_404, redirect
from contact.models import Contact
from django.db.models import Q


import contact

# Create your views here.
def index(request):
    contacts = Contact.objects.filter(show=True).order_by('id')
    
    context = {
        'contacts': contacts,
        'site_title': 'Contatos - '
         
    }
    
    return render(request, 'contact/index.html', context)

def search(request):
    search_value = request.GET.get('q', '').strip()
    
    if search_value == '':
        return redirect('contact:index')
   
    contacts = Contact.objects.filter(show=True).filter(Q(firt_name__icontains=search_value) | 
                                                        Q(last_name__icontains=search_value) |
                                                        Q(phone__icontains=search_value) |
                                                        Q(email__icontains=search_value)
                                                        )\
                                                            .order_by('id')
    
    context = {
        'contacts': contacts,
        'site_title': 'Contatos - '
         
    }
    
    return render(request, 'contact/index.html', context)


def contact(request, contact_id):
    single_contact = get_object_or_404(Contact, pk=contact_id, show=True)
    
    titulo = f'{single_contact.firt_name} {single_contact.last_name} - '
    
    context = {
        'contact': single_contact,
        'site_title': titulo,
    
    }
    return render(request, 'contact/contact.html', context)
