from cProfile import label
from email import errors
from django.shortcuts import render, redirect, get_object_or_404
from contact.models import Contact
from django import forms
from django.core.exceptions import ValidationError
from django.urls import reverse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from django.contrib.auth import authenticate, login, password_validation
from django.contrib import auth, messages

class ContactForm(forms.ModelForm):
    phone = forms.CharField(
        validators=[
            RegexValidator(
                regex=r'^\d{11}$',  # Aceita apenas números com exatamente 11 dígitos
                message='O telefone deve conter exatamente 11 dígitos numéricos.'
            )
        ],
        label="Telefone",
        help_text="Digite o número de telefone com 11 dígitos, incluindo o DDD (ex: 11987654321)."
    )
    picture = forms.ImageField(
        label= 'Imagem',
        help_text= 'Escolha uma imagem para adicionar ao contato (opcional).',
        required=False,
        widget=forms.FileInput(attrs={
            'accept' : 'image/*',
        })
        )
    
    class Meta:
        model = Contact
        fields = ('firt_name', 'last_name', 'phone',
                  'email','description', 'category', 'picture')
        labels = {
            'firt_name': 'Nome',
            'last_name': 'Sobrenome',
            'phone': 'Telefone',
            'email': 'E-mail',
            'description': 'Descrição',
            'category': 'Categoria',
        }
        
        
    def clean(self):
        cleaned_data = self.cleaned_data
        firt_name = cleaned_data.get('firt_name')
        last_name = cleaned_data.get('last_name')

        if firt_name == last_name:
            msg = ValidationError(
                'Primeiro nome não pode ser igual ao segundo',
                code='invalid'
            )
            
            msgl = ValidationError(
                'Segundo nome igual ao Primeiro',
                code='invalid'
            )
            self.add_error('firt_name', msg)
            self.add_error('last_name', msgl)

        return super().clean()
    
    def clean_firt_name(self):
        cleaned_data = self.cleaned_data
        firt_name = cleaned_data.get('firt_name')
        msgf = ValidationError('ABC, não é um nome valido', code='invalid')
        if firt_name == 'ABC':
            self.add_error('firt_name', msgf)
            
        return firt_name

class RegisterForm(UserCreationForm):
    firt_name = forms.CharField(required=True,label='Nome', min_length=3)
    last_name = forms.CharField(required=True,label='Sobrenome' ,min_length=3)
    email = forms.EmailField()
    
    class Meta:
        model = User
        fields = (
            'firt_name', 'last_name', 'email','username', 'password1', 'password2',
        )
        
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            self.add_error(
                'email', ValidationError('E-mail já cadastrado', code='invalid')
            )
            return email
        return('contact/register.html')
    
    
    
class RegisterUpdateForm(forms.ModelForm):
    first_name = forms.CharField(
        label="Nome",
        min_length=2,
        max_length=30,
        required=True,
        help_text='Obrigatorio.',
        error_messages={
            'min_length': 'Por favor, adicionar pelo menos 2 letras.'
        }
    )
    last_name = forms.CharField(
        label="Sobrenome",
        min_length=2,
        max_length=30,
        required=True,
        help_text='Obrigatorio'
    )

    password1 = forms.CharField(
        label="Senha",
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "nova-senha"}),
        help_text=password_validation.password_validators_help_text_html(),
        required=False,
    )

    password2 = forms.CharField(
        label="Confirme a senha",
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "nova-senha"}),
        help_text='Use a mesma senha de antes.',
        required=False,
    )

    class Meta:
        model = User
        fields = (
            'first_name', 'last_name', 'email',
            'username',
        )

    def save(self, commit=True):
        cleaned_data = self.cleaned_data
        user = super().save(commit=False)
        password = cleaned_data.get('password1')

        if password:
            user.set_password(password)

        if commit:
            user.save()

        return user

    def clean(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 or password2:
            if password1 != password2:
                self.add_error(
                    'password2',
                    ValidationError('Senhas devem ser iguais')
                )

        return super().clean()

    def clean_email(self):
        email = self.cleaned_data.get('email')
        current_email = self.instance.email

        if current_email != email:
            if User.objects.filter(email=email).exists():
                self.add_error(
                    'email',
                    ValidationError('E-mail ja registrado', code='invalid')
                )

        return email
    
    
    def clean_password1(self):
        password1 = self.cleaned_data.get('password1')
        
        if password1:
            try:
                password_validation.validate_password(password1)
            except ValidationError as errors:
                self.add_error('password1', ValidationError(errors))
                
        return password1
    
def create(request):
    form_action = reverse('contact:create')
    if request.method == 'POST':
        form = ContactForm(request.POST, request.FILES)
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
        form = ContactForm(request.POST, request.FILES, instance=contact,)
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



def delete(request, contact_id):
    contact = get_object_or_404(
        Contact, pk=contact_id, show=True
    )
    confirmacao = request.POST.get('confirmacao', 'nao')

    if confirmacao == 'sim':
        contact.delete()
        return redirect('contact:index')

    return render(
        request,
        'contact/contact.html',
        {
            'contact': contact,
            'confirmacao': confirmacao,
        }
    )
    
