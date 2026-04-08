from django.shortcuts import render, redirect

# Create your views here.
def t_dashboard(request):
    if request.user.is_authenticated:
        print('authenticated')
        name = request.user.username
        info = {
            "username": name,
        }
        return render(request, 'pages/teacher_dashboard.html', info)
    return redirect('/login')