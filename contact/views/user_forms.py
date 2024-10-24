from django.contrib import auth, messages
from django.shortcuts import redirect, render
from contact.views import RegisterForm
from django.shortcuts import render, redirect, get_object_or_404



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