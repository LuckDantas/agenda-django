from django.db import models
from django.contrib.auth.models import User

# Create your models here.
#Criando o banco de dados
class Evento(models.Model):
        titulo = models.CharField(max_length=100, null=True)
        descricao = models.TextField(blank=True, null=True)
        data_evento = models.DateTimeField(verbose_name="DATA DO EVENTO")
        data_criacao = models.DateTimeField(auto_now=True)
        usuario = models.ForeignKey(User, on_delete=models.CASCADE) #SE O USUÁRIO FOR EXCLUIDO EXCLUIR TUDO QUE É DEPENDENCIA DELE;

        #Caso você tenha um banco de dados que necessite que a tabela tenha um nome específico
        class Meta:
                db_table="evento"

        #Sempre que chamar o objeto retorna o título.
        def __str__(self):
                return self.titulo

        def get_data_evento(self):
                return self.data_evento.strftime('%d/%m/%Y')