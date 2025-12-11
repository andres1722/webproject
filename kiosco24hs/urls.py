from django.urls import path
from . import views

urlpatterns = [
    path('info/', views.info,name = 'info'),
    path('',views.home, name = 'home'), 
    path('stores/',views.stores_v,name = 'stores'),
    path('products/',views.products_v,name = 'products'),
    path('create_store/',views.create_store,name ='create_store'),
    path('create_products/',views.create_products,name ='create_products'),
    path('contact/', views.contact, name='contact'),
    path('details/<int:id>',views.details, name='details')
   
    
]