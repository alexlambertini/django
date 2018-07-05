from django.db import models
from taggit.managers import TaggableManager

# Create your models here.


class Post(models.Model):
    titulo = models.CharField(max_length=50)
    texto = models.TextField()
    data = models.DateTimeField()
    tags = TaggableManager()
    imagem = models.ImageField(upload_to='post_imagens', null=True, blank=True)
    slug = models.SlugField(max_length=100, blank=True)

    def __str__(self):
        post = self.titulo
        return post


class Menu(models.Model):
    titulo_menu = models.CharField(max_length=50)

    def __str__(self):
        menus = self.titulo_menu
        return menus
