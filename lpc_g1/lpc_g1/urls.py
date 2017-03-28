"""lpc_g1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
#from lpc_g1.views import *

urlpatterns = [
    url(r'^admin/', admin.site.urls),


    url(r'^eventos/([0-9])/', eventoId, name='eventoId'),
    url(r'^eventos/', evento, name='evento'),
    url(r'^eventoCientifico/([0-9])/',eventoCientificoId, name='eventoCientificoId'),
    url(r'^eventoCientifico/', eventoCientifico, name='eventoCientifico'),
    url(r'^pessoa/([0-9])/',pessoaId , name='pessoaId'),s
    url(r'^pessoa/',pessoa , name='pessoa'),
    url(r'^pessoaFisica/([0-9])/', pessoaFisicaId, name='pessoaFisicaId'),
    url(r'^pessoaFisica/', pessoaFisica, name='pessoaFisica'),
    url(r'^pessoaJuridica/([0-9])/', pessoaJuridicaId, name='pessoaJuridicaId'),
    url(r'^pessoaJuridica/', pessoaJuridica, name='pessoaJuridica'),
    url(r'^autor/([0-9])/', autorId, name='autorId'),
    url(r'^autor/', autor, name='autor'),
    url(r'^artigoCientifico/([0-9])/', artigoCientificoId, name='artigoCientificoId'),
    url(r'^artigoCientifico/', artigoCientifico, name='artigoCientifico'),

]
