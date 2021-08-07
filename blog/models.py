from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    #CharField indica a quantidade de strings que o campo (Post) pode receber.
    title = models.CharField(max_length=255)
    # SlugField é o texto usado na URL do Post
    slug = models.SlugField(max_length=255, unique=True)
    # on_delete é o que acontece com a postagem se o usuário for deletado e o CASCADE é para deletar a postagem junto.
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    #Corpo do Post - TextField está vazio para poder escrever o quanto quiser no Post.
    body = models.TextField()
    #auto_now_add=True - serve para adicionar automaticamente a data e a hora de quando o artigo foi criado.
    created = models.DateTimeField(auto_now_add=True)
    # Serve para atualizar o campo automaticamente quando o artigo for editado.
    update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
        
