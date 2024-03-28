from django.db import models

class Acao(models.Model):
    nome = models.CharField(max_length=50)
    media = models.FloatField()
    desvio_padrao = models.FloatField()
    coef_variacao = models.FloatField()

    def __str__(self):
        return self.nome

