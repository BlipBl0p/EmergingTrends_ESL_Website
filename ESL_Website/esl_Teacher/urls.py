from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.t_dashboard, name = 't_dashboard'),
    path('students/', views.t_studentlist, name = 't_studentlist'),
    path('grades/', views.t_grades, name = 't_grades'),
    path('dashboard/modules/', views.t_modules, name = 't_modules'),
    path('dashboard/modules/add-lesson/', views.t_addlessons, name = 't_addlessons'),
    path('dashboard/add-module/', views.t_addmodules, name = 't_addmodules'),
]