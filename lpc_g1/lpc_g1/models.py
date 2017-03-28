from django.db import models
from django.utils import timezone


class Pessoa(models.Model):
    nomeP = models.CharField('nomeP', max_length=200)
    email = models.CharField('nomeP', max_length=200)

    def save(self, *args, **kwargs):
        self.nomeP = self.nomeP.upper()
        self.email = self.local.upper()

        super(Pessoa, self).save(*args, **kwargs)

    def __str__(self):
        return '{}'.format(self.nomeP)


class Evento(models.Model):
    nome = models.CharField('nome', max_length=200)
    eventoPrincipal = models.CharField('eventoPrincipal',max_length=200)
    sigla = models.CharFild('sigla',max_length=200)
    dataEHoraDeInicio = models.DateTimeField('dataEHoraDeInicio', default=timezone.now)
    palavraChave = models.CharFild('palavraChave',max_length=200)
    logoTipo = models.CharFild('logoTipo',max_length=200)
    realizador = models.ForeignKey('Pessoa')
    cidade = models.CharFild('cidade',max_length=200)
    uf= models.CharFild('uf',max_length=200)
    endereco = models.CharFild('endereco',max_length=200)
    cep = models.CharFild('cep',max_length=200)

    def save(self, *args, **kwargs):
        self.nome = self.nome.upper()
        self.eventoPrincipal = self.eventoPrincipal.upper()

        super(Evento, self).save(*args, **kwargs)

    def __str__(self):
        return '{}'.format(self.nome)


class ArtigoCientifico(models.Model):
    titulo = models.CharField('titulo', max_length=200)
    altores = models.Array('altores')
    evento = models.ForeignKey('EventoCientifico')

    def save(self, *args, **kwargs):
        self.titulo = self.titulo.upper()
        self.altores = self.altores.upper()

        super(ArtigoCientifico, self).save(*args, **kwargs)

    def __str__(self):
        return '{}'.format(self.titulo)

class EventoCientifico(models.Eventos):
    issn = models.CharField('issn', max_length=200)

    def save(self, *args, **kwargs):
        self.issn = self.issn.upper()

        super(EventoCientifico, self).save(*args, **kwargs)

    def __str__(self):
        return '{}'.format(self.issn)


class Altor(models.Pessoa):
    curriculo = models.CharField('curriculo', max_length=200)
    artigo = models.Array('artigos')

    def save(self, *args, **kwargs):
        self.curriculo = self.curriculo.upper()
        self.artigo = self.artigo.upper()

        super(Pessoa, self).save(*args, **kwargs)

    def __str__(self):
        return '{}'.format(self.curriculo)

class PessoaFisica(models.Pessoa):
    cpf = models.CharField('cpf', max_length=200)

    def save(self, *args, **kwargs):
        self.cpf = self.cpf.upper()

        super(Pessoa, self).save(*args, **kwargs)

    def __str__(self):
        return '{}'.format(self.cpf)

class PessoaJuridica(models.Pessoa):
    cnpj = models.CharField('cnpj', max_length=200)
    razaoSocial = models.CharField('razaoSocial', max_length=200)

    def save(self, *args, **kwargs):
        self.cnpj = self.cnpj.upper()
        self.razaoSocial = self.razaoSocial.upper()

        super(Pessoa, self).save(*args, **kwargs)

    def __str__(self):
        return '{}'.format(self.cnpj)

class Inscricao(models.PessoaFisica):
    dataHoraIscicao = models.DateTimeField('dataHoraIscicao')
    tipoIscriçcao =  models.CharField('tipoIscricao', max_length=200)

#######################################################################################
