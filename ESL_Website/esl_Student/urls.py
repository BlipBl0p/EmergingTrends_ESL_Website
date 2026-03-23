from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.s_dashboard, name = 's_dashboard'),
]