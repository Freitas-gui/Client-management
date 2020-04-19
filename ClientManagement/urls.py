from django.contrib import admin
from django.urls import path, include
from Clients import urls as Clients_urls
from home import urls as home_urls
from django.conf import settings
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('home/',include(home_urls)),
    path('admin/', admin.site.urls),
    path('person/',include(Clients_urls)),
    path('login/', auth_views.LoginView.as_view(), name='url_login'),
]
