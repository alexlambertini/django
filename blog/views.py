from django.shortcuts import render
from .models import Post
from .models import Menu

# Create your views here.


def Home(request):
    posts = Post.objects.all().order_by("-data")
    menus = Menu.objects.all()
    return render(request, 'blog.html', {'posts': posts, 'menus': menus,})
