from django.contrib import admin
from .models import Post
from .models import Menu

class AutoSlug(admin.ModelAdmin):
    prepopulated_fields = {'slug' : ('titulo',)}

# Register your models here.
admin.site.register(Post, AutoSlug)
admin.site.register(Menu)
