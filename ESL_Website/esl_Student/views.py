from django.shortcuts import render, redirect

# Create your views here.
def s_dashboard(request):
    if request.user.is_authenticated:
        return render(request, 'pages/student_dashboard.html')
    return redirect('/login')