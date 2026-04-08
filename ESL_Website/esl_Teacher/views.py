from django.shortcuts import render

# Create your views here.
def t_dashboard(request):
    if request.user.is_authenticated:
        return render(request, 'pages/teacher_dashboard.html')
    return redirect('/login')