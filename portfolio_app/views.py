from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from .models import Project, Service

def home(request):
    projects = Project.objects.all().order_by('-created_at')[:4]
    services = Service.objects.all()
    return render(request, 'portfolio_app/porto.html', {
        'projects': projects,
        'services': services
    })

