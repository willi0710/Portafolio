from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html')

def explaboral(request):   
    return render(request, 'explaboral.html')