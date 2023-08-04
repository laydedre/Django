from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request,'home.html')

def gerenciar(request):
    return render(request,'gerenciar.html')

def cadastrar_banco(request):
    apelido = request.POST.get('apelido')
    banco = request.POST.get('banco')
    tipo = request.POST.get('tipo')
    valor = request.POST.get('valor')
    icone = request.POST.get('icone')
    
    