from django.shortcuts import render

# Create your views here.
def s_dashboard(request):
    return render(request, 'pages/student_dashboard.html')