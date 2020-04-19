from django.contrib import admin
from django.urls import path, include
from Clients import urls as Clients_urls
from .views import persons_list , update , create , delete

urlpatterns = [
    path('list/', persons_list , name = 'url_persons_list'),
    path('update/<int:pk>/', update , name = 'url_update'),
    path('create/', create , name ='url_create'),
    path('delete/<int:pk>/', delete , name = 'url_delete'),
]