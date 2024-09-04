from django.shortcuts import render

import contact

# Create your views here.
def index(request):
    return render(request, 'contact/index.html',)
