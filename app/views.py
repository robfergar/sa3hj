from django.shortcuts import render

# Create your views here.

def index(request):

    return render(request,'app/index.html')

def sobre(request):

    return render(request,'app/sobre.html')

def contato(request):

    return render(request,'app/contato.html')

