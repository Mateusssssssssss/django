from django.contrib import auth, messages
from django.shortcuts import redirect, render
from contact.views import RegisterForm, RegisterUpdateForm
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required




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
            messages.success(request,f'Login efetuado com sucesso')
            return redirect('contact:index')
            
        else:
            messages.error(request, 'Nome de usuário ou senha incorretos.')
    
    return render(request,'contact/login.html',{
        'form': form
    })
    
def logout_views(request):
    auth.logout(request)
    messages.success(request, 'Logout feito com sucesso')
    return redirect('contact:login')

@login_required(login_url='contact:login')
def user_update(request):
    if not request.user.is_authenticated:
         return redirect('contact:login')
     
    form =  RegisterUpdateForm(instance=request.user)
        
    if request.method == 'POST':
        form = RegisterUpdateForm(request.POST, instance=request.user)
        
        if form.is_valid():
            form.save()
            messages.success(request, 'Usuario atualizado com sucesso')
            return redirect('contact:index')
         
    return render(request,'contact/update_user.html',
                  {
                      'form': form,

                  })
    
    