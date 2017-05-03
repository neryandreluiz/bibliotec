from django.shortcuts import render, render_to_response
from .models import Livro

# Create your views here.

def listar_livros(request):
    livros = Livro.objects.all()
    return render_to_response("livros.html", {"livros":livros})
