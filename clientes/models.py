from django.db import models

# Create your models here.


class Person(models.Model):
    primeiro_nome = models.CharField(max_length=30)
    ultimo_nome = models.CharField(max_length=30)
    idade = models.IntegerField()
    bio = models.TextField()
    foto = models.ImageField(upload_to='clientes_fotos', null=True, blank=True)

    def __str__(self):
        nome = self.primeiro_nome + ' ' + self.ultimo_nome
        return nome

