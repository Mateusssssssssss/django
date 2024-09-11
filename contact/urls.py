
from contact import views
from django.urls import path

app_name ='contact'

urlpatterns = [
    path('<int:contact_id>/', views.contact, name='contact'),
    path('', views.index, name='index'),
    
]