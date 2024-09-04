
from contact import views
from django.urls import path

app_name ='contact'

urlpatterns = [
    path('', views.index, name='index'),
]