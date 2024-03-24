from django.urls import path

from . import views


urlpatterns = [
    path('login', views.auth_login, name='auth_login'),
    path('register', views.auth_register, name='auth_register'),
    path('change-password', views.change_password, name='change_password'),
    path('logout', views.auth_logout, name='auth_logout'),
]
