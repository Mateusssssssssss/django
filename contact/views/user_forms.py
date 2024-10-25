from django.contrib import auth, messages
from django.shortcuts import redirect, render
from contact.views import RegisterForm
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm



def register(request):
    form = RegisterForm()
  
    
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Usuario Registrado')
            return redirect('contact:index')
    return render(request,'contact/register.html',
                  {
                      'form': form,

                  })
    
def login( request):
    form = AuthenticationForm(request)
    
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        
        if form.is_valid():
            user = form.get_user()
            messages.success(request, 'Login efetuado com sucesso')
            return redirect('contact:index')  # Redireciona para a página inicial ou outra página desejada
        else:
            messages.error(request, 'Nome de usuário ou senha incorretos.')
    
    return render(request,'contact/login.html',{
        'form': form
    })
    