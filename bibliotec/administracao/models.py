
from django.db import models

class Livro(models.Model):
    id_livro = models.AutoField(primary_key=True, blank=False, null=False)
    titulo = models.CharField(max_length=250, verbose_name="Título",blank=False, null=False)
    autor = models.CharField(max_length=150, verbose_name="Autor",blank=False, null=False)
    editora = models.CharField(max_length=150, verbose_name="Editora",blank=True, null=True)
    ano_publicacao = models.IntegerField(verbose_name="Ano",blank=True, null=True)
    edicao = models.IntegerField(verbose_name="Edição",blank=False, null=False)
    isbn = models.CharField(max_length=13, verbose_name="ISBN",blank=False, null=False)
    sinopse = models.TextField(verbose_name="Sinopse",blank=True, null=True)


    def __str__(self):
        return self.titulo