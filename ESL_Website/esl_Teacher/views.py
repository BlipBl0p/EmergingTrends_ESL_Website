from django.shortcuts import render

# Create your views here.
def t_dashboard(request):
    return render(request, 'pages/teacher_dashboard.html')