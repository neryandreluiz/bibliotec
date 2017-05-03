
from django.db import models

#Para tornar o exemplo o mais simples possível, não está sendo feito nenhum tipo de validação dos campos dos modelos.

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


class Cliente(models.Model):
    id_cliente = models.AutoField(primary_key=True, blank=False, null=False)
    nome = models.CharField(max_length=250)
    cpf = models.CharField(max_length=14) #padrão: xxx.xxx.xxx-xx
    endereco = models.CharField(max_length=300)
    telefone = models.CharField(max_length=15) #padrão: (xx) xxxxx-xxxx

    def __str__(self):
        return self.nome


class Reserva(models.Model):
    id_reserva = models.AutoField(primary_key=True, blank=False, null=False)
    livro = models.ForeignKey(Livro)
    cliente = models.ForeignKey(Cliente)
    data_reserva = models.DateField("Data de Início", auto_now=True)

    def __str__(self):
        return "Reserva: {0} - {1} - {2}".format(self.id_reserva, self.livro, self.cliente)
