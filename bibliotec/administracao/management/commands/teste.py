from django.core.management.base import BaseCommand, CommandError
from administracao.models import Livro

class Command(BaseCommand):

    def metodo_testes(self):
        
        #Listando objetos:
        # o = Livro.objects.all()
        # for i in o:
        #     print(i)

        #Criando objetos:
        livro = Livro(titulo="Meu primeiro livro",
                      autor="Bruno Oliveira",
                      editora="O'REILLY NovaTec",
                      ano_publicacao=2018,
                      edicao=1,
                      isbn=23451,
                      sinopse="Este livro bla bla bla...")
        livro.save()
        print(livro)

    def handle(self, *args, **options):
        self.metodo_testes()