from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from core.models import Evento
from django.contrib.auth import authenticate, logout, login
from django.contrib.messages import error


# Create your views here.

#def index(request):
#    return redirect('/agenda')

#Se o usuário não estiver autenticado não conseguirá acessar. NECESSÁRIO LOGIN
 #Necessário redirecionar para a página de login
def login_user(request):
    return render(request, 'login.html')

@login_required(login_url='/login/') #requer que seja no elemento
def lista_eventos(request):
    usuario = request.user  #necessário estar autenticado para filtrar por usuário.
    evento = Evento.objects.filter(usuario=usuario) #Evento.objects.all()
    dados = {'eventos': evento}
    return render(request, 'agenda.html', dados)

#authenticação
def submit_login(request):
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        usuario = authenticate(username=username, password=password)
        if usuario is not None:
            login(request, usuario)
            return redirect('/')

        else:
            messages.error(request, "Usuário ou senha inválido.")
    return redirect('/')

def logout_user(request):
    logout(request)
    return redirect('/')

@login_required(login_url='/login/') #requer que seja no elemento
def evento(request):
    return render(request, 'evento.html')

@login_required(login_url='/login/') #requer que seja no elemento
def submit_evento(request):
    if request.POST: #apenas aceitar métodos POST (evitar invasão ou inserção de código)
        titulo = request.POST.get('titulo')
        data_evento = request.POST.get('data_evento')
        descricao = request.POST.get('descricao')
        usuario = request.user
        #SALVAR NO BANCO DE DADOS (CREATE)
        Evento.objects.create(titulo=titulo, data_evento=data_evento, descricao=descricao, usuario=usuario)

    return redirect('/')