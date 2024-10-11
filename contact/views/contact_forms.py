from django.shortcuts import render, redirect
from contact.models import Contact
from django import forms
from django.core.exceptions import ValidationError



class ContactForm(forms.ModelForm):
    
    class Meta:
        model = Contact
        fields = ('firt_name', 'last_name', 'phone',
                  'email','description', 'category',)
        
    

def create(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        
        context = {
        'form': form
        }
        if form.is_valid():
            form.save()
            
            return redirect('contact:create')
    
        return render(request,'contact/create.html', context)
    
    context = {
        'form' : ContactForm()
        }
    return render(request,'contact/create.html', context)


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