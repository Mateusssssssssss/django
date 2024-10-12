from django.shortcuts import render, redirect, get_object_or_404
from contact.models import Contact
from django import forms
from django.core.exceptions import ValidationError
from django.urls import reverse



class ContactForm(forms.ModelForm):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    
    class Meta:
        model = Contact
        fields = ('firt_name', 'last_name', 'phone',
                  'email','description', 'category',)
        
    

def create(request):
    form_action = reverse('contact:create')
    if request.method == 'POST':
        form = ContactForm(request.POST)
        context = {
            'form': form,
            'form_action': form_action,
        }
        if form.is_valid():
            contact = form.save()
            return redirect('contact:update', contact_id=contact.pk)
        return render(request, 'contact/create.html', context)
    
    context = {
        'form': ContactForm(),
        'form_action': form_action,
    }
    return render(request, 'contact/create.html', context)


def update(request, contact_id):
    contact = get_object_or_404(Contact, pk=contact_id, show=True)
    form_action = reverse('contact:update', args=(contact_id,))
    
    if request.method == 'POST':
        form = ContactForm(request.POST, instance=contact)
        context = {
            'form': form,
            'form_action': form_action,
        }
        if form.is_valid():
            contact = form.save()
            return redirect('contact:update', contact_id=contact.pk)
        return render(request, 'contact/create.html', context)
    
    context = {
        'form': ContactForm(instance=contact),
        'form_action': form_action,
    }
    return render(request, 'contact/create.html', context)



def clean(self):
        # cleaned_data = self.cleaned_data
    cleaned_data = self.cleaned_data
    first_name = cleaned_data.get('first_name')
    last_name = cleaned_data.get('last_name')
        
    if first_name == last_name:
        msg = ValidationError(
        'Primeiro nome não pode ser igual ao segundo',
        code='invalid')
        self.add_error('first_name', msg)
        self.add_error('last_name', msg)

        return super().clean()

def clean_first_name(self):
    first_name = self.cleaned_data.get('first_name')
    if first_name == 'ABC':
        self.add_error(
            'firt_name',
            ValidationError(
                'Veio do add_error',
                code='invalid'
            )
        )
    return first_name