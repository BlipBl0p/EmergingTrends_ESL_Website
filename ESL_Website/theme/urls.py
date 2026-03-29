from django.urls import path
from . import views

urlpatterns = [
    path('', views.loginpage, name = 'login'),
    path('login/', views.loginpage, name = 'login'),
    path('logout/', views.logoutpage, name = 'logout')
]