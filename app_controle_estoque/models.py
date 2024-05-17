from django.db import models


class Item(models.Model):
    id_item = models.AutoField(primary_key=True)
    nome = models.TextField(max_length=255, blank=False)
    quantidade = models.TextField(max_length=10, blank=False)
    unidade = models.TextField(max_length=10, blank=False)
    validade = models.TextField(max_length=10, blank=False)

def __str__(self):
        return self.nome