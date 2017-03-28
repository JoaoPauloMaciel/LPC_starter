from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt, csrf_protect

from .models import *


def inicio(request):
    html = """<h1>Opções</h1>
                <ul>
                    <li><a href='/evento'>Eventos</a></li>
                    <li><a href='/atividade'>Atividades</a></li>
                    <li><a href='/tipoatividades'>Tipo de Atividade</a></li>
                </ul>
            """
    return HttpResponse(html)

@csrf_exempt
def addTipoAtividade(request):
    html = "<h1>Adicionar Atividades</h1>"
    if request.method == 'POST':
        tipo = TipoAtividade()
        tipo.descricao = request.POST['descricao']
        tipo.save()
        return HttpResponse('Tipo Inserido com sucesso')
    else:
        return HttpResponse('Falha na inserção de tipo')


def listaTipoAtividades(request):
    html = "<h1><a href='http://localhost:8000/'>Lista de Tipo de Atividades</a></h1>"
    lista = TipoAtividade.objects.all()
    for tipo in lista:
        html += '<li>|  {}  |  {}  |  {}  </li>'.format(tipo.id,tipo.descricao, tipo.data_cadastro)

    return HttpResponse(html)

def evento(request):
    html = "<h1><a href='http://localhost:8000/'>Eventos</a></h1>"
    lista = Evento.objects.all()
        for tipo in lista:
            html += '<li>|  {}  |  {}  |  {}  |  {}  |  {}  |  {}  |  {}  |  {}  |  {}  |  {}  |  {}  |  {}</li>'.format(tipo.id, tipo.nome, tipo.local, tipo.abertura_evento, tipo.encerramento_evento, tipo.abertura_inscricoes, tipo.encerramento_inscricoes, tipo.limite_inscricoes, tipo.apresentacao, tipo.publico_alvo, tipo.programacao, tipo.data_cadastro)

    return HttpResponse(html)

def atividade(request):
        html = "<h1><a href='http://localhost:8000/'>Atividades</a></h1>"
        lista = Atividade.objects.all()
        for tipo in lista:
            html += '<li>|  {}  |  {}  |  {}</li>'.format(tipo.id,tipo.tema,tipo.descricao)

        return HttpResponse(html)

##############################################################################################################################

def eventoId(request,id):
    retorna = "<h1><a href='http://localhost:8000/'>Eventos</a></h1>"
    ident=Evento.objects.get(pk=id)
    lista = Evento.objects.all()
    for tipo in lista
        if (str(ident) == tipo.nome):
            retorna += '<li>|  {}  |  {}  |  {}  |  {}  |  {}  |  {}  |  {}  |  {}  |  {}  |  {}  |  {}  |  {}</li>'.format(tipo.id, tipo.nome, tipo.local, tipo.abertura_evento, tipo.encerramento_evento, tipo.abertura_inscricoes, tipo.encerramento_inscricoes, tipo.limite_inscricoes, tipo.apresentacao, tipo.publico_alvo, tipo.programacao, tipo.data_cadastro)
    return HttpResponse(retorna)

def atividadeId(request,id):
    retorna = "<h1><a href='http://localhost:8000/'>Atividades</a></h1>"
    ident=Atividade.objects.get(pk=id)
    lista = Atividade.objects.all()
    for tipo in lista:
        if (str(ident) == tipo.tema):
            retorna += '<li>|  {}  |  {}  |  {}</li>'.format(tipo.id,tipo.tema,tipo.descricao)
    return HttpResponse(retorna)

def  listaTipoAtividadesId(request,id):
    retorna = "<h1><a href='http://localhost:8000/'>Tipo de Atividades da Lista</a></h1>"
    ident=TipoAtividade.objects.get(pk=id)
    lista = TipoAtividade.objects.all()
    for tipo in lista:
        if (str(ident) == tipo.descricao):
            retorna += '<li>|  {}  |  {}  |  {}</li>'.format(tipo.id,tipo.descricao,tipo.data_cadastro)
    return HttpResponse(retorna)
