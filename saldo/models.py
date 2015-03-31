from django.db import models

class Professor(models.Model):
    nome = models.CharField(max_length=60)
    def __unicode__(self):
        return self.nome

class Encargo(models.Model):
    professor = models.ForeignKey(Professor)
    ano = models.CharField(max_length=4)
    sem = models.CharField(max_length=1)
    horas = models.FloatField(default=0)
    encargos = models.FloatField(default=0)
    pontos = models.FloatField(default=0)
    somar = models.FloatField(default=0)
    saldo_i = models.FloatField(default=0)
    saldo_f = models.FloatField(default=0)
    def __unicode__(self):
        return self.professor.nome + " " + self.ano + "/" + self.sem

class Media(models.Model):
    somapt = models.FloatField(default=0)
    nelementos = models.IntegerField(default=0)
    media = models.FloatField(default=0)
    anosem = models.CharField(max_length=6)
    def __unicode__(self):
        return str(self.media)