from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt, csrf_protect

from .models import *

def evento(request):
    html = "<h1><a href='http://localhost:8000/'>Eventos</a></h1>"
    lista = Evento.objects.all()
    for tipo in lista:
        html += '<li>|  {}  |  {}  |  {}  </li>'.format(tipo.id,tipo.descricao, tipo.data_cadastro)
    return HttpResponse(html)

def eventoId(request):
    retorna = "<h1><a href='http://localhost:8000/'>Eventos</a></h1>"
    ident=Evento.objects.get(pk=id)
    lista = Evento.objects.all()
    for tipo in lista
        if (str(ident) == tipo.nome):
            retorna += '<li>|  {}  |  {}  |  {}  |  {}  |  {}  |  {}  |  {}  |  {}  |  {}  |  {}  |  {}  |  {}</li>'.format(tipo.id, tipo.nome, tipo.local, tipo.abertura_evento, tipo.encerramento_evento, tipo.abertura_inscricoes, tipo.encerramento_inscricoes, tipo.limite_inscricoes, tipo.apresentacao, tipo.publico_alvo, tipo.programacao, tipo.data_cadastro)
    return HttpResponse(retorna)
