from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.t_dashboard, name = 't_dashboard'),
    path('students/', views.t_studentlist, name = 't_studentlist'),
    path('grades/', views.t_grades, name = 't_grades'),
]