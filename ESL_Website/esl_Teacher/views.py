from django.shortcuts import render, redirect
import datetime

# Create your views here.
def t_dashboard(request):
    if request.user.is_authenticated:
        name = request.user.username
        today = datetime.datetime.now().strftime("%b %e")
        info = {
            "username": name,
            "today": today
        }
        return render(request, 'pages/teacher_dashboard.html', info)
    return redirect('/login')

def t_studentlist(request):
    if request.user.is_authenticated:
        return render(request, 'pages/teacher_studentlist.html')
    return redirect('/login')

def t_grades(request):
    if request.user.is_authenticated:
        return render(request, 'pages/teacher_grades.html')
    return redirect('/login')