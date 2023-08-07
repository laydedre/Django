from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.messages import constants
from perfil.models import Conta

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
    
    if len(apelido.strip()) == 0 or len(valor.strip()) == 0:
        return redirect('/perfil/gerenciar')
    
    conta = Conta(
        apelido = apelido,
        banco = banco,
        tipo = tipo,
        valor = valor,
        icone = icone
    )
    
    conta.save()
    
    return redirect('/perfil/gerenciar')