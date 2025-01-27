from django.db import models

# Create your models here.

class PontoColeta(models.Model):
    nome = models.CharField(max_length=200)
    descricao = models.TextField()
    endereco = models.CharField(max_length=255)
    latitude = models.FloatField()
    longitude = models.FloatField()

    def __str__(self):
        return self.nome