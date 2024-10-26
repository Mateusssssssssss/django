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
    
def login_views(request):
    form = AuthenticationForm(request)
    
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth.login(request, user)
            messages.success(request,f'Logado com sucesso')
            
        else:
            messages.error(request, 'Nome de usuário ou senha incorretos.')
    
    return render(request,'contact/login.html',{
        'form': form
    })
    
def logout_views(request):
    auth.logout(request)
    messages.success(request, 'Logout feito com sucesso')
    return redirect('contact:login')
    