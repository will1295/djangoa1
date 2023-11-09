from django.shortcuts import render
from .models import Alumnos

# Create your views here.
def home(request):
    alumnos = Alumnos.objects.all()
    return render(request,"pagina.html",{"alumnos":alumnos})
