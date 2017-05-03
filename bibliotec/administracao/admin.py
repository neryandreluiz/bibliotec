from django.contrib import admin
from .models import Livro

# Register your models here.
class AdminLivro(admin.ModelAdmin):
    search_fields = ('titulo','autor')
    list_display = ('titulo', 'autor', 'sinopse',)
    exclude = ('ISBN',)
    actions_on_bottom = True
    actions_on_top = False

admin.site.register(Livro,AdminLivro)
