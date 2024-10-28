
from contact import views
from django.urls import path

app_name ='contact'

urlpatterns = [
    
    path('search/', views.search, name='search'),
    path('', views.index, name='index'),
    
    #CRUD
    path('contact/<int:contact_id>/', views.contact, name='contact'),
    path('contact/create/', views.create , name='create'),
    path('contact/<int:contact_id>/update/', views.update, name='update'),
    path('contact/<int:contact_id>/delete/', views.delete, name='delete'),
    #USER
    path('user/create/', views.register , name='register'),
    path('user/login/', views.login_views, name='login'),
    path('user/logout/', views.logout_views, name='logout'),
    path('user/update/', views.user_update, name='user_update'),
    #path('<int:contact_id>/update/', views.contact, name='contact'),
    #path('<int:contact_id>/delete/', views.contact, name='contact'),
    
]