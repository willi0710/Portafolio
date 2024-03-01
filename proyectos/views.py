from django.shortcuts import render, get_object_or_404
from .models import Proyecto
# Create your views here.

def project_render(request):
    projects= Proyecto.objects.all()
    return render(request, 'proyectos.html', {'projects': projects})